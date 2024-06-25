from flask import Blueprint, request
from auth.controls import AuthController
from flask_jwt_extended import jwt_required, get_jwt_identity

auth = Blueprint('auth', __name__)
auth_controller = AuthController()


@auth.post('/api/register/')
def register():
    data = request.get_json()
    res = auth_controller.create_user(data)
    return res


@auth.post('/api/login/')
def login():
    data = request.get_json()
    return auth_controller.get_user_jwt_token(data)


@auth.route('/api/refresh/')
@jwt_required(refresh=True)
def refresh_token():
    identity = get_jwt_identity()
    return auth_controller.refresh_access_jwt_token(identity)


@auth.route('/api/login-verification')
def login_verification():
    token = request.headers.get("Authorization")
    return auth_controller.verification_user_token(token)
