class DevConfig():
    SECRET_KEY = """4C4t*bKvtPrb=u+Nl7.J%a&~pjd4'GdGOX#by1$Y<L33J<VC;p`U@37TaXA7$Rf"""
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///storage_test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
