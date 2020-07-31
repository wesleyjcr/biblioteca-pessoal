from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def init_app(app):
    db = SQLAlchemy(app)
    Migrate(app, db)
