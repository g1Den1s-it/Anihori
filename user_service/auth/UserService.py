from auth.models import User
from auth import db
from flask import abort
from sqlalchemy import update


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

    def update_data(self, user, **kwargs) -> None:
        try:
            valid_keys = {key for key in kwargs.keys() if hasattr(user, key)}

            if valid_keys:
                db.session.execute(
                    update(User)
                    .where(User.id == user.id)
                    .values({key: kwargs[key] for key in valid_keys})
                )
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, {"message": e})

    def load_user(self, data) -> User | None:
        try:
            user = User.query.filter_by(email=data['email']).first()
            return user
        except:
            return None
