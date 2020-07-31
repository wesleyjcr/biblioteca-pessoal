from flask import Flask
from biblioteca.ext import configuration
from biblioteca.ext import database
from biblioteca.ext import auth
from biblioteca.blueprints import api


def create_app():
    app = Flask(__name__)

    configuration.init_app(app)
    database.init_app(app)
    auth.init_app(app)
    api.init_app(app)

    return app
