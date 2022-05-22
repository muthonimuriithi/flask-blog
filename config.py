import os
class config:
        
        SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://bless:123@localhost/blog"
        SECRET_KEY =('SECRET_KEY')
        MAIL_SERVER = 'smtp.gmail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = False
        MAIL_USE_SSL = True
        MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
        MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
        
        UPLOADED_PHOTOS_DEST = "app/static/photos"


class ProdConfig(config):

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://bless:123@localhost/blog"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class DevConfig(config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    DEBUG= True
    ENV = 'development'
    

config_options = {
    'production': ProdConfig,
    'development': DevConfig

    }