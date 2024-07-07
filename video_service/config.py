import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    DEBUG = os.getenv("FLASK_DEBUG")
