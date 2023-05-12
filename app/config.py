import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    pass

class DevelopmentConfig(Config):
    pass

config = {
    'development': DevelopmentConfig
}