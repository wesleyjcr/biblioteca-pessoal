from flask import jsonify, request
from biblioteca.ext.database import db
from biblioteca.models import Author
from flask_jwt_extended import jwt_required


@jwt_required
def register_author():
    data = request.get_json()

    author = Author()
    author.name = data["name"]

    db.session.add(author)

    try:
        db.session.commit()
        return jsonify({"name": author.name}), 201
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
