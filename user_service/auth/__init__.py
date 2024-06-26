from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
login_manager = LoginManager()
jwt = JWTManager()


def create_app(config):
    app = Flask(__name__)

    app.config.from_prefixed_env()
    app.config.from_object(config)

    db.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)

    # service auth
    from auth.routers import auth
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    return app
