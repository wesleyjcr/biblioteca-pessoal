class ProdConfig():
    FLASK_APP = "biblioteca/app.py"
    SECRET_KEY = """4C4t*bKvtPrb=u+Nl7.J%a&~pjd4'GdGOX#by1$Y<L33J<VC;p`U@37TaXA7$Rf"""
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///../storage.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig():
    SECRET_KEY = """4C4t*bKvtPrb=u+Nl7.Ja&~pjd4'GdGOX#by1$Y<L33J<VC;p`U@37TaXA7$Rf"""
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///../storage_dev.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
