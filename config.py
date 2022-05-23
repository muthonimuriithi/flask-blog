import os
class config:
        
         
        SECRET_KEY =os.environ.get('SECRET_KEY')
        MAIL_SERVER = 'smtp.gmail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = False
        MAIL_USE_SSL = True
        MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
        MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
        
        
        UPLOADED_PHOTOS_DEST = "app/static/photos"


class ProdConfig(config):
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)

    SQLALCHEMY_DATABASE_URI = uri
    
    

class DevConfig(config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    DEBUG= True
    ENV = 'development'
    

config_options = {
    'production': ProdConfig,
    'development': DevConfig

    }