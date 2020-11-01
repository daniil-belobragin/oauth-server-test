from authlib.oauth2 import OAuth2Error
from flask.views import MethodView
from flask import request, session, render_template
from werkzeug.exceptions import Unauthorized
from util.oauth import authorization
from service.user import UserService


class OAuthCallback(MethodView):

    def get(self):
        print(request.args)

        return {}


class OAuthAuthorize(MethodView):

    def get(self):
        if "id" not in session:
            raise Unauthorized()

        user = UserService.get(session["id"])

        try:
            grant = authorization.validate_consent_request(end_user=user)
        except OAuth2Error as e:
            return e.error

        return render_template('authorize.html', user=user, grant=grant)

    def post(self):
        if "id" not in session:
            raise Unauthorized()

        user = UserService.get(session["id"])

        return authorization.create_authorization_response(grant_user=user)


class IssueToken(MethodView):

    def post(self):

        return authorization.create_token_response()
