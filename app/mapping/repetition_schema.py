from app.models import Repetition
from marshmallow import fields, Schema, post_load

class RepetitionSchema(Schema):
    id = fields.Integer(dump_only=True)
    workout_id = fields.Integer(required=True)
    excercise_id = fields.Integer(required=True)
    series_number = fields.Integer(required=True)
    num_repetitions = fields.List(fields.Integer(), required=True)
    peso = fields.Float()

    @post_load
    def make_repetition(self, data, **kwargs):
        return Repetition(**data)