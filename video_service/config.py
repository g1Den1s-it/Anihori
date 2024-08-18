import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    DEBUG = os.getenv("FLASK_DEBUG")
    ALLOWED_EXTENSIONS = ['mp4']
    UPLOAD_FOLDER = 'static'


class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    DEBUG = os.getenv("FLASK_DEBUG")
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("FLASK_JWT_SECRET_KEY")
