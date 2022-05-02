from pytest import raises
from pydantic import SecretStr
from faker import Faker
from harubooru.service_providers.config_provider import PostgresqlConfig, MysqlConfig, SqliteConfig
from harubooru.service_providers.database_provider import make_connection_url


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
    def test_make_sqlite_connection_url(tmp_path):
        config = SqliteConfig(driver='sqlite', file_path=tmp_path)
        assert make_connection_url(config) == f'sqlite:///{tmp_path}'
