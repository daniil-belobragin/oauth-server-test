import time
from flask import session, request
from flask.views import MethodView

from werkzeug.exceptions import Unauthorized
from werkzeug.security import gen_salt

from service.client import OAuth2ClientService
from util.validator import json_body_validator
from schema import CreateClientSchema


class CreateClient(MethodView):

    def post(self):
        if "id" not in session:
            raise Unauthorized()

        body = json_body_validator(CreateClientSchema)

        user_id = session["id"]

        client_id = gen_salt(24)
        client_secret = gen_salt(48)
        client_id_issued_at = time.time()

        client_name = body.get("client_name", "default_app")
        client_uri = body["client_uri"]
        redirect_uri = body["redirect_uri"]

        client_metadata = {
            "client_name": client_name,
            "client_uri": client_uri,
            "redirect_uris": [redirect_uri],
            "grant_types": ["authorization_code"],
            "response_types": ["code"],
            "scope": "profile",
            "token_endpoint_auth_method": "client_secret_basic"

        }

        oauth2_client = OAuth2ClientService.add(client_id, client_secret, client_id_issued_at, user_id,
                                                client_metadata)

        return {
            "data": oauth2_client.to_dict()
        }
