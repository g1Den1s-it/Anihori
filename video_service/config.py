import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    DEBUG = os.getenv("FLASK_DEBUG")
    ALLOWED_EXTENSIONS = ['mp4']
    UPLOAD_FOLDER = 'static'
    JWT_SECRET_KEY = os.getenv("FLASK_JWT_SECRET_KEY")


class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    DEBUG = True
    SECRET_KEY = "f41a3cef74487fffe5ab8e63c1a49f4e2cc0707c694427b50edc54"
    JWT_SECRET_KEY = "f41a3cef74487fffe5ab8e63c1a49f4e2cc0707c694427b50edc54"
