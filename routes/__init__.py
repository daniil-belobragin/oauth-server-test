from view.session import Signin, LogOut
from view.client import CreateClient
from view.oauth import OAuthCallback, OAuthAuthorize, IssueToken
from view.user import User


def register(app):
    app.add_url_rule("/signin", view_func=Signin.as_view("signin"))
    app.add_url_rule("/logout", view_func=LogOut.as_view("logout"))
    app.add_url_rule("/create-client", view_func=CreateClient.as_view("create_client"))
    app.add_url_rule("/oauth", view_func=OAuthCallback.as_view("oauth"))
    app.add_url_rule("/oauth/authorize", view_func=OAuthAuthorize.as_view("oauth_authorize"))
    app.add_url_rule("/oauth/token", view_func=IssueToken.as_view("issue_token"))
    app.add_url_rule("/user", view_func=User.as_view("user"))
