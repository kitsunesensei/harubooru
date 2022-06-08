from pytest import raises
from pydantic import SecretStr
from faker import Faker
from sqlalchemy import Column, Integer, text
from sqlalchemy.orm.session import Session as BaseSession
from fastapi import Depends
from harubooru.service_providers.config_provider import PostgresqlConfig, MysqlConfig, SqliteConfig
from harubooru.service_providers.database_provider import BaseModel, make_connection_url, init, get_session


class TestMakeConnectionUrl:
    @staticmethod
    def test_make_malicious_connection_url():
        with raises(TypeError):
            make_connection_url()
            make_connection_url({})

    @staticmethod
    def test_make_postgresql_connection_url(faker: Faker):
        (host, user, pw, db,) = (faker.hostname(), faker.user_name(), faker.password(), faker.slug())
        config = PostgresqlConfig(driver='postgresql', host=host, username=user, password=pw, database=db)
        assert make_connection_url(config) == f'postgresql+psycopg2://{user}:{pw}@{host}:5432/{db}'
        assert isinstance(config.password, SecretStr)

        (host, user, pw, db, port,) = (faker.hostname(), faker.user_name(), faker.password(), faker.slug(),
                                       faker.port_number())
        config = PostgresqlConfig(driver='postgresql', host=host, username=user, password=pw, database=db, port=port)
        assert make_connection_url(config) == f'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'

    @staticmethod
    def test_make_mysql_connection_url(faker: Faker):
        (host, user, pw, db,) = (faker.hostname(), faker.user_name(), faker.password(), faker.slug())
        config = MysqlConfig(driver='mysql', host=host, username=user, password=pw, database=db)
        assert make_connection_url(config) == f'mysql://{user}:{pw}@{host}:3306/{db}'
        assert isinstance(config.password, SecretStr)

        (host, user, pw, db, port,) = (faker.hostname(), faker.user_name(), faker.password(), faker.slug(),
                                       faker.port_number())
        config = MysqlConfig(driver='mysql', host=host, username=user, password=pw, database=db, port=port)
        assert make_connection_url(config) == f'mysql://{user}:{pw}@{host}:{port}/{db}'

    @staticmethod
    def test_make_sqlite_connection_url(tmp_path, faker: Faker):
        file_path = f'{tmp_path}/{faker.sha1(raw_output=False)}.sqlite'
        config = SqliteConfig(driver='sqlite', file_path=file_path)
        assert make_connection_url(config) == f'sqlite:///{file_path}'


class TestDbInit:
    @staticmethod
    def test_init_session_instance(tmp_path, faker: Faker):
        db_config = SqliteConfig(file_path=f'{tmp_path}/{faker.sha1(raw_output=False)}.sqlite')
        Session = init(db_config)()
        assert isinstance(Session, BaseSession)

    @staticmethod
    def test_init_model_create(tmp_path, faker: Faker):
        class TestTable(BaseModel):
            __tablename__ = f'table_{faker.sha1(raw_output=False)}'
            id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

        db_config = SqliteConfig(file_path=f'{tmp_path}/{faker.sha1(raw_output=False)}.sqlite')
        Session = init(db_config)()

        assert list(BaseModel.metadata.tables.keys()).index(TestTable.__tablename__) >= 0

        query = text(f'SELECT name FROM sqlite_schema WHERE type=\'table\' AND name=\'{TestTable.__tablename__}\';')
        result = Session.execute(query).mappings().all()
        assert len(result) == 1
        assert result[0].name == TestTable.__tablename__


class TestGetSession:
    @staticmethod
    def test_get_session_infused(tmp_path, faker: Faker):
        # db_config = SqliteConfig(file_path=f'{tmp_path}/{faker.sha1(raw_output=False)}.sqlite')
        # Session = init(db_config)
        #
        # app.dependency_overrides[BaseSession] = Session
        #
        # session = get_session()
        #
        # object_methods = [method_name for method_name in dir(session)
        #                   if callable(getattr(session, method_name))]
        # print(object_methods)
        # assert session.add()
        assert False
