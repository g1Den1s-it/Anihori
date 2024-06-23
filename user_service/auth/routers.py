from flask import Blueprint, request

from auth.controls import AuthController

auth = Blueprint('auth', __name__)


@auth.get('/api/register/')
def register():
    data = request.get_json()
    auth_controller = AuthController()
    res = auth_controller.create_user(data)
    return res
