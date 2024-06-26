import os
import jwt
from flask import jsonify, Response
from flask import abort
from auth.UserService import UserService
from auth.models import User
from flask_jwt_extended import create_access_token, create_refresh_token


class AuthController:
    def __init__(self):
        self.user_service = UserService()

    def create_user(self, data) -> Response:
        if not (data['username'] and data['email'] and data['password']):
            abort(400, {"message": "required username, email and password"})

        if User.query.filter_by(email=data['email']).first():
            abort(400, {"message": "This Email already exist!"})

        user = self.user_service.create_user_object(data['username'], data['email'], data['password'])

        return jsonify(user.to_dict())

    def get_user_jwt_token(self, user_data) -> Response:
        user = self.user_service.load_user(user_data)

        if user and user.verify_password(user_data['password']):
            access_token = create_access_token(identity=user.to_dict())
            refresh_token = create_refresh_token(identity=user.to_dict())

            return jsonify({
                "access": access_token,
                "refresh": refresh_token
            })
        return jsonify({"message": "this user does not exist"})

    def refresh_access_jwt_token(self, identity) -> Response:
        access_token = create_access_token(identity=identity)
        return jsonify({"access": access_token})

    def verification_user_token(self, token: str) -> tuple[Response, int]:
        if not token:
            return jsonify({'message': "Token is missing"}), 401

        parts_token = token.split(" ")

        if len(parts_token) != 2:
            return jsonify({"message": "Invalid token format"}), 401

        is_valid_token = self.__verify_jwt_token(parts_token[1])

        if is_valid_token:
            return jsonify({"message": "Valid"}), 200
        else:
            return jsonify({"message": "Invalid"}), 401


    def __verify_jwt_token(self, jwt_token):
        try:
            payload = jwt.decode(
                jwt_token,
                os.getenv("FLASK_JWT_SECRET_KEY"),
                "HS256"
            )
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
