import marshmallow


class SignInSchema(marshmallow.Schema):
    email = marshmallow.fields.String(required=True)


class CreateClientSchema(marshmallow.Schema):
    client_uri = marshmallow.fields.String(required=True)
    redirect_uri = marshmallow.fields.String(required=True)
