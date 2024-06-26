from auth import db
from passlib.apps import custom_app_context


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    username = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def hash_password(self, password: str) -> None:
        self.password = custom_app_context.hash(password)

    def verify_password(self, password: str) -> bool:
        return custom_app_context.verify(password, self.password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
