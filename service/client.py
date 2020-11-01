from uuid import uuid4

from model.oauth import OAuth2Client
from model import db


class OAuth2ClientService:

    @classmethod
    def add(cls, client_id, client_secret, client_id_issued_at, user_id,
            client_metadata):
        c_id = str(uuid4())
        oauth2_client = OAuth2Client(c_id, client_id, client_secret, client_id_issued_at, user_id)
        oauth2_client.set_client_metadata(client_metadata)
        db.session.add(oauth2_client)
        db.session.commit()

        return oauth2_client
