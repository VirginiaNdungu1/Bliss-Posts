# initialise flask
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_option):
    # initialise application
    app = Flask(__name__)

    # create app configurations
    app.config.from_object(config_options[config_option])

    # initialise flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    # Register Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app
