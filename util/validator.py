from flask import request


def json_body_validator(schema):
    body = request.json
    schema_instance = schema()
    schema_instance.load(body)
    return body


def url_params_validator(schema):
    url_params = request.args
    schema_instance = schema()
    schema_instance.load(url_params)
    return url_params
