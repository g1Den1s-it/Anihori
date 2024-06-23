from auth.models import User
from auth import db
from flask import abort


class UserService:

    def create_user_object(self, username: str, email: str, password: str) -> User:
        try:
            user = User(username=username, email=email)
            user.hash_password(password)

            db.session.add(user)
            db.session.flush()
            db.session.commit()

            return user
        except Exception as e:
            db.session.rollback()
            abort(500, {"message": e})
