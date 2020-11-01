from flask import session
from flask.views import MethodView
from werkzeug.exceptions import Unauthorized

from service.user import UserService
from util.validator import json_body_validator
from schema import SignInSchema


class Signin(MethodView):

    def post(self):
        body = json_body_validator(SignInSchema)

        username = body.get("username", "Guest")
        email = body["email"]

        if UserService.exists_by_email(email):
            user = UserService.get_by_email(email)
            session["id"] = user.id

            return {
                "data": user.to_dict()
            }

        user = UserService.add(username, email)
        session["id"] = user.id

        return {
            "data": user.to_dict()
        }


class LogOut(MethodView):

    def delete(self):
        if "id" not in session:
            raise Unauthorized()

        user = UserService.get(session["id"])
        del session["id"]

        return {
            "data": user.to_dict()
        }
