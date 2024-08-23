import os
from datetime import timedelta



class Config:
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=8)
    JWT_SECRET_KEY = os.getenv("FLASK_JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
    DEBUG = os.getenv("FLASK_DEBUG")
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")


class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    DEBUG = True
    SECRET_KEY = "f41a3cef74487fffe5ab8e63c1a49f4e2cc0707c694427b50edc54"
    JWT_SECRET_KEY = "f41a3cef74487fffe5ab8e63c1a49f4e2cc0707c694427b50edc54"
