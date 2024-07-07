from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config=None):
    app = Flask(__name__)

    if not config:
        app.config.from_prefixed_env()
    app.config.from_object(config)

    db.init_app(app)

    from anime.routers import anime
    app.register_blueprint(anime)

    with app.app_context():
        db.create_all()

    return app
