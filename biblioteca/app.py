from flask import Flask
from biblioteca.ext import database
from biblioteca.ext import auth
from biblioteca.blueprints import api


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.DevConfig')
   
    database.init_app(app)
    auth.init_app(app)
    api.init_app(app)
    
    return app


