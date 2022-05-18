class config:
    pass

class ProdConfig(config):

    pass

class DevConfig(config):

    pass

    DEBUG= True
    ENV = 'development'

config_options = {
    'production': ProdConfig,
    'development': DevConfig

    }