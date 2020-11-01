import time
from uuid import uuid4

from authlib.integrations.sqla_oauth2 import OAuth2ClientMixin, OAuth2AuthorizationCodeMixin, \
    OAuth2TokenMixin
from sqlalchemy_serializer import SerializerMixin

from model import db


class OAuth2Client(db.Model, OAuth2ClientMixin, SerializerMixin):
    __tablename__ = "oauth2_client"

    id = db.Column(db.String, primary_key=True)
    client_id = db.Column(db.String, unique=True)
    client_secret = db.Column(db.String, unique=True)
    client_id_issued_at = db.Column(db.Integer)
    user_id = db.Column(db.String, db.ForeignKey("users.id", ondelete="CASCADE"))

    user = db.relationship("User")

    def __init__(self, c_id, client_id, client_secret, client_id_issued_at, user_id):
        self.id = c_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_id_issued_at = client_id_issued_at
        self.user_id = user_id


class OAuth2AuthorizationCode(db.Model, SerializerMixin, OAuth2AuthorizationCodeMixin):
    __tablename__ = "oauth2_code"

    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey("users.id", ondelete="CASCADE"))

    user = db.relationship("User")


class OAuth2Token(db.Model, OAuth2TokenMixin, SerializerMixin):
    __tablename__ = 'oauth2_token'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.String, db.ForeignKey('users.id', ondelete='CASCADE'))

    user = db.relationship('User')

    def is_refresh_token_active(self):
        if self.revoked:
            return False
        expires_at = self.issued_at + self.expires_in * 2
        return expires_at >= time.time()
