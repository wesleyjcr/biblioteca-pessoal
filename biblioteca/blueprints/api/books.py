from flask import jsonify, request, abort
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
            "id": book.id,
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


@jwt_required
def get_book_by_id(book_id):
    book = Books.query.filter(Books.id == book_id).one_or_none()
    if book:
        author = Author.query.filter_by(id=book.author_id).first()
        data = {
            "id": book.id,
            "author": author.name,
            "amount": book.amount,
            "cover": book.cover,
            "title": book.title
        }
        return jsonify(book=data)
    else:
        abort(404, f'Livro com Id: {book_id} não foi encontrado')


@jwt_required
def update_book(book_id):
    new_data = request.get_json()
    book = Books.query.filter(Books.id == book_id).first()

    if book:
        if 'title' in new_data:
            book.title = new_data['title']
        if 'cover' in new_data:
            book.cover = new_data['cover']
        if 'amount' in new_data:
            book.amount = new_data['amount']
        if 'author' in new_data:
            book.author_id = new_data['author']
        db.session.commit()

        book = Books.query.filter(Books.id == book_id).first()
        data = {
            "author": book.author_id,
            "amount": book.amount,
            "cover": book.cover,
            "title": book.title
        }

        return jsonify(data)
    else:
        abort(404, f'Livro com Id: {book_id} não foi encontrado')


@jwt_required
def delete_book(book_id):
    book = Books.query.filter(Books.id == book_id).first()
    db.session.delete(book)
    db.session.commit()
    return f'Registro de Id: {book_id} removido com sucesso!', 204
