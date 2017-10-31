import os


class Config:
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://monster:Hummingbirdcomp#@localhost/bliss_posts'
    DEBUG = True


class ProdConfig(Config):
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://monster:Hummingbirdcomp#@localhost/bliss_posts_test'


config_options = {
    'production': ProdConfig,
    'development': DevConfig,
    'test': TestConfig
}
