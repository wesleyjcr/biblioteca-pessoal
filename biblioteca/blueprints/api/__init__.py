from flask import Blueprint, jsonify
from biblioteca.blueprints.api.author import uai_so
from biblioteca.blueprints.api.user import login, register, protected

bp = Blueprint('api', __name__, url_prefix='/api/v1')


def init_app(app):
    app.register_blueprint(bp)


routes = [
    ('/uai', 'uai_so', uai_so, ["GET"]),
    ('/test', 'test', test, ["GET"]),
    ('/login', 'login', login, ["GET", "POST"]),
    ('/register', 'register', register, ["POST"]),
    ('/protected', 'protected', protected, ["GET"])
]


for route, endpoint, view_func, methods in routes:
    bp.add_url_rule(
        route,
        endpoint,
        view_func,
        methods=methods)
