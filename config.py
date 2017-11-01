import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://monster:Hummingbirdcomp#@localhost/bliss_posts'
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://monster:Hummingbirdcomp#@localhost/bliss_posts_test'


config_options = {
    'production': ProdConfig,
    'development': DevConfig,
    'test': TestConfig
}
