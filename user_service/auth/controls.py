from flask import jsonify, Response
from flask import abort
from auth.UserService import UserService
from auth.models import User


class AuthController:

    def create_user(self, data) -> Response:
        if not (data['username'] and data['email'] and data['password']):
            abort(400, {"message": "required username, email and password"})

        if User.query.filter_by(email=data['email']).first().exeist():
            abort(400, {"message": "This Email already exist!"})

        user_service = UserService()
        user = user_service.create_user_object(data['username'], data['email'], data['password'])

        return jsonify(user.to_dict())
