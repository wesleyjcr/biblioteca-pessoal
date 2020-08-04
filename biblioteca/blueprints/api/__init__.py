from flask import Blueprint
from biblioteca.blueprints.api.author import register_author
from biblioteca.blueprints.api.user import login, register, protected
from biblioteca.blueprints.api.books import register_book, get_all_books

bp = Blueprint('api', __name__, url_prefix='/api/v1')


def init_app(app):
    app.register_blueprint(bp)


routes = [
    ('/login', 'login', login, ["GET", "POST"]),
    ('/register', 'register', register, ["POST"]),
    ('/protected', 'protected', protected, ["GET"]),
    ('/register_author', 'register_author', register_author, ["POST"]),
    ('/register_book', 'register_book', register_book, ["POST"]),
    ('/get_all_books', 'get_all_books', get_all_books, ["GET"])
]


for route, endpoint, view_func, methods in routes:
    bp.add_url_rule(
        route,
        endpoint,
        view_func,
        methods=methods)
