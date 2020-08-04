from flask import jsonify, request
from biblioteca.ext.database import db
from biblioteca.models import Books, Author
from flask_jwt_extended import jwt_required


@jwt_required
def register_book():
    data = request.get_json()

    book = Books()
    book.title = data["title"]
    book.author_id = data["author_id"]
    book.amount = data["amount"]
    book.cover = data["cover"]

    author = Author.query.filter_by(id=data["author_id"]).first()

    db.session.add(book)

    try:
        db.session.commit()
        return jsonify({
            "title": book.title,
            "author": author.name,
            "amount": book.amount,
            "cover": book.cover}), 201
    except Exception as error:
        print(error)
        return (
            jsonify(
                {
                    "message": "Por algum motivo não conseguimos fazer o cadastro do autor.",
                    "statusCode": 500,
                }
            ),
            500,
        )


@jwt_required
def get_all_books():
    books = Books.query.all()
    data = []
    for book in books:
        author = Author.query.filter_by(id=book.author_id).first()
        data.append({
            "id": book.id,
            "author": author.name,
            "amount": book.amount,
            "cover": book.cover,
            "title": book.title
        })
    return jsonify(list_books=data)
