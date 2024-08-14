from app.models import Workout
from marshmallow import fields, Schema, post_load

class WorkoutSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    date_time = fields.DateTime(required=True)
    name_workout = fields.String(required=True)

    @post_load
    def make_workout(self, data, **kwargs):
        return Workout(**data)