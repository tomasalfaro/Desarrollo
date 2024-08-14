from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Workout(db.Model):
    __tablename__ = 'workouts'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_time: str = db.Column(db.DateTime, nullable=False)
    name_workout: str = db.Column(db.String(120), nullable=False)