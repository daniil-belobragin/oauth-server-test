from model import db
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, u_id, username, email):
        self.id = u_id
        self.username = username
        self.email = email

    def get_user_id(self):
        return self.id
