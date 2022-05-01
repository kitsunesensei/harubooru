from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from harubooru.service_providers.config_provider import application_config as config, PostgresqlConfig, MysqlConfig, \
    SqlLiteConfig, LogLevels


def make_connection_url(db_config: PostgresqlConfig | MysqlConfig | SqlLiteConfig) -> str:
    if isinstance(db_config, PostgresqlConfig):
        return f'postgresql+psycopg2://{db_config.username}:{db_config.password.get_secret_value()}' \
               f'@{db_config.host}:{db_config.port}/{db_config.database}'

    if isinstance(db_config, MysqlConfig):
        return f'mysql://{db_config.username}:{db_config.password.get_secret_value()}' \
               f'@{db_config.host}:{db_config.port}/{db_config.database}'

    if isinstance(db_config, SqlLiteConfig):
        return f'sqlite:///{db_config.file_path}'

    raise TypeError('Unknown Database Driver.')


engine = create_engine(make_connection_url(config.database), echo=config.log_level is LogLevels.DEBUG)

database_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModel = declarative_base()

BaseModel.metadata.create_all(bind=engine)
