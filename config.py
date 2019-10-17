class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = "YOUR_URI"