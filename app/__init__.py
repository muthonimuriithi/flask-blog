from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

bootstrap = Bootstrap()

db = SQLAlchemy()

def create_app (environment):
    app = Flask(__name__)
    bootstrap.init_app(app)

    app.config.from_object(config_options[environment])
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


