from flask import jsonify, request
from datetime import timedelta
from biblioteca.ext.database import db
from biblioteca.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, create_access_token


def login():
    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()
    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify(
            {"msg": "Ops, algo deu errado! Verifique os dados informados"}
        )

    payload = {
        "id": user.id,
    }
    access_token = create_access_token(
        payload, expires_delta=timedelta(minutes=2))
    return jsonify({"access_token": access_token, "statusCode": 201}), 201


def register():
    data = request.get_json()

    user = User()
    user.email = data["email"]
    user.name = data["name"]
    user.password = generate_password_hash(data["password"])

    db.session.add(user)

    try:
        db.session.commit()
        return jsonify({"name": user.name, "email": user.email, }), 201
    except Exception as error:
        print(error)
        return (
            jsonify(
                {
                    "message": "Por algum motivo não conseguimos fazer o cadastro do usuário.",
                    "statusCode": 500,
                }
            ),
            500,
        )


@jwt_required
def protected():
    return "Rota protegida."
