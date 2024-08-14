from app.models import Excercise
from marshmallow import fields, Schema, post_load

class ExcerciseSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    workout_id = fields.Integer(required=True)

    @post_load
    def make_excercise(self, data, **kwargs):
        return Excercise(**data)