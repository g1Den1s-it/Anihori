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
    DEBUG = os.getenv("FLASK_DEBUG")
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("FLASK_JWT_SECRET_KEY")
