from app.models import User
from marshmallow import fields, Schema, post_load

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)