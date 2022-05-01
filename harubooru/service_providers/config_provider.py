from enum import Enum
from typing import Any, Dict, Literal, Tuple
from pathlib import Path
import yaml
from pydantic import BaseModel, BaseSettings, SecretStr, AnyHttpUrl, FilePath, DirectoryPath, AnyUrl, IPvAnyAddress
from pydantic.env_settings import SettingsSourceCallable


def parse_yml(config_object: BaseSettings) -> Dict[str, Any]:
    with open(Path('config.yml'), 'r', encoding=config_object.__config__.env_file_encoding) as stream:
        return yaml.safe_load(stream)


class AppEnvironments(str, Enum):
    PRODUCTION = 'production'
    STAGING = 'staging'
    TEST = 'test'
    LOCAL = 'local'


class LogLevels(str, Enum):
    CRITICAL = 'critical'
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'
    DEBUG = 'debug'
    DISABLED = 'notset'


class MysqlConfig(BaseModel):
    driver: Literal['mysql']
    host: AnyUrl | IPvAnyAddress
    username: str
    password: SecretStr
    database: str
    port: int = 3306


class PostgresqlConfig(BaseModel):
    driver: Literal['postgresql']
    host: AnyUrl | IPvAnyAddress
    username: str
    password: SecretStr
    database: str
    port: int = 5432


class SqlLiteConfig(BaseModel):
    driver: Literal['sqllite']
    file_path: Path


class LocalStorageConfig(BaseModel):
    driver: Literal['local']
    base_path: DirectoryPath


class WebdavStorageConfig(BaseModel):
    driver: Literal['webdav']
    url: AnyHttpUrl
    username: str
    password: SecretStr
    connection_timeout: int = 30
    proxy_hostname: AnyHttpUrl
    proxy_username: str
    proxy_password: SecretStr
    cert_path: FilePath | None = None
    key_path: FilePath | None = None
    disable_check: bool = False
    download_chunk_size: int = 65536


class ApplicationConfig(BaseSettings):
    config_file: FilePath = 'config.yml'
    app_environment: AppEnvironments = AppEnvironments.PRODUCTION
    log_level: LogLevels | Tuple[LogLevels] = LogLevels.CRITICAL

    database: MysqlConfig | PostgresqlConfig | SqlLiteConfig
    storage: Dict[str, LocalStorageConfig | WebdavStorageConfig]

    class Config:  # pylint: disable=too-few-public-methods
        env_prefix = 'harubooru_'

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,  # pylint: disable=unused-argument
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable
        ) -> Tuple[SettingsSourceCallable, ...]:
            return (
                env_settings,
                parse_yml,
                file_secret_settings
            )


application_config = ApplicationConfig()
