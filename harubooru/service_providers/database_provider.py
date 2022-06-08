from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from harubooru.service_providers.config_provider import application_config, PostgresqlConfig, MysqlConfig, \
    SqliteConfig, LogLevels

BaseModel = declarative_base()


def make_connection_url(db_config: PostgresqlConfig | MysqlConfig | SqliteConfig) -> str:
    if isinstance(db_config, PostgresqlConfig):
        return f'postgresql+psycopg2://{db_config.username}:{db_config.password.get_secret_value()}' \
               f'@{db_config.host}:{db_config.port}/{db_config.database}'

    if isinstance(db_config, MysqlConfig):
        return f'mysql://{db_config.username}:{db_config.password.get_secret_value()}' \
               f'@{db_config.host}:{db_config.port}/{db_config.database}'

    if isinstance(db_config, SqliteConfig):
        return f'sqlite:///{db_config.file_path}'

    raise TypeError('Unknown Database Driver.')


def init(
    db_config: PostgresqlConfig | MysqlConfig | SqliteConfig,
    print_output: bool = application_config.log_level is LogLevels.DEBUG
):
    engine = create_engine(make_connection_url(db_config), echo=print_output)
    Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)  # pylint: disable=invalid-name
    BaseModel.metadata.create_all(bind=engine)
    return Session


SessionMaker = init(application_config.database, application_config.log_level)


def get_session(session_maker: SessionMaker = Depends()):
    with session_maker() as session:
        yield session
