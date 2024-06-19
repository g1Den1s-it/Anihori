from flask import Blueprint


auth = Blueprint('auth', __name__)


@auth.get('/')
def hello():
    return "<h1>Hello World!</h1>"
