from flask.views import MethodView
from authlib.integrations.flask_oauth2 import current_token
from util.oauth import require_oauth


class User(MethodView):

    @require_oauth('profile')
    def get(self):
        user = current_token.user

        return {
            "data": user.to_dict()
        }
