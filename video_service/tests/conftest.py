import pytest
from anime import create_app, db as _db
from config import TestConfig


class User(_db.Model):
    __tablename__ = 'users'
    id = _db.Column(_db.Integer, primary_key=True)


@pytest.fixture()
def app():
    app = create_app(TestConfig)

    with app.app_context():
        _db.create_all()
        yield app

        _db.session.remove()
        _db.drop_all()


@pytest.fixture()
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.session.remove()
        _db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
