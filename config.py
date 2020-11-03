import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joan:Turquoise1@localhost/management'
    

class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}