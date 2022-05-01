from harubooru.service_providers.config_provider import application_config, ApplicationConfig, \
    LocalStorageConfig, WebdavStorageConfig


class Driver:
    pass


class LocalFileDriver(Driver):
    pass


class WebdavDriver(Driver):
    pass


class FileHandler:
    config: ApplicationConfig
    connections: (Driver, ...)

    def __init__(self, config: ApplicationConfig):
        self.config = config

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    @staticmethod
    def resolve_driver(config: LocalStorageConfig | WebdavStorageConfig):
        if isinstance(config, LocalStorageConfig):
            return LocalFileDriver

        if isinstance(config, WebdavStorageConfig):
            return WebdavDriver

        raise TypeError('Unknown Storage Driver.')


file_handler = FileHandler(application_config)
