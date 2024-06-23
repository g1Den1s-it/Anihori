from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'qwdnrtfsgrqdgwerhew12!#@wefqwefwe'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://anihori:qwerty@db:5432/anihori_db"

    db.init_app(app)
    login_manager.init_app(app)

    # service auth
    from auth.routers import auth
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    return app
