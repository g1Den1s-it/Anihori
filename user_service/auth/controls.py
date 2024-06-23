from flask import request, jsonify, Response
from flask import abort
from auth.UserSercvice import UserService


class AuthController:

    def create_user(self, data) -> Response:
        if not (data['username'] and data['email'] and data['password']):
            abort(400, {"message": "required username, email and password"})

        user_service = UserService()
        user = user_service.create_user_object(data['username'], data['email'], data['password'])

        return jsonify(user.to_dict())
