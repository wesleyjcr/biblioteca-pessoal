from flask import Blueprint
from biblioteca.blueprints.api.author import register_author
from biblioteca.blueprints.api.user import login, register, protected
from biblioteca.blueprints.api.books import (
    register_book,
    get_all_books,
    get_book_by_id,
    update_book,
    delete_book,
)

bp = Blueprint("api", __name__, url_prefix="/api/v1")


def init_app(app):
    app.register_blueprint(bp)


routes = [
    ("/login", "login", login, ["GET", "POST"]),
    ("/register", "register", register, ["POST"]),
    ("/protected", "protected", protected, ["GET"]),
    ("/register_author", "register_author", register_author, ["POST"]),
    ("/books", "register_book", register_book, ["POST"]),
    ("/books", "get_all_books", get_all_books, ["GET"]),
    ("/books/<book_id>", "update_book", update_book, ["PATCH"]),
    ("/books/<book_id>", "delete_book", delete_book, ["DELETE"]),
    ("/books/<book_id>", "get_book_by_id", get_book_by_id, ["GET"]),
]


for route, endpoint, view_func, methods in routes:
    bp.add_url_rule(route, endpoint, view_func, methods=methods)
