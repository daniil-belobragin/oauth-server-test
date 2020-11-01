from flask import Flask
from werkzeug.exceptions import HTTPException
from marshmallow.exceptions import ValidationError

from routes import register
from model import db
from util.oauth import config_oauth

app = Flask(__name__)
app.config.update({
    "SECRET_KEY": "secret",
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
})

register(app)
db.init_app(app)
config_oauth(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(HTTPException)
def handle_error_response(e):
    return {"response": e.description}, e.code


@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return {"response": e.messages}, 422


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=777)
