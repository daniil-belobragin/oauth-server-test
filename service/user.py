from uuid import uuid4

from model import db
from model.user import User


class UserService:

    @classmethod
    def add(cls, username, email):
        u_id = str(uuid4())

        user = User(u_id, username, email)
        db.session.add(user)
        db.session.commit()

        return user

    @classmethod
    def get(cls, u_id):
        return db.session.query(User).filter(User.id == u_id).first()

    @classmethod
    def remove(cls, u_id):
        user = cls.get(u_id)
        db.session.delete(user)
        db.session.commit()

        return user

    @classmethod
    def exists_by_email(cls, email):
        return db.session.query(db.exists().where(User.email == email)).scalar()

    @classmethod
    def get_by_email(cls, email):
        return db.session.query(User).filter(User.email == email).first()

    @classmethod
    def get_by_username(cls, username):
        return db.session.query(User).filter(User.username == username).first()
