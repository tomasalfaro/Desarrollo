from dataclasses import dataclass
from sqlalchemy import PickleType
from app import db

@dataclass(init=False, repr=True, eq=True)
class Repetition(db.Model):
    __tablename__ = 'repetitions'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    workout_id: int = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    excercise_id: int = db.Column(db.Integer, db.ForeignKey('excercises.id'), nullable=False)
    series_number: int = db.Column(db.Integer, nullable=False)
    num_repetitions: PickleType = db.Column(PickleType, nullable=False)
    peso: float = db.Column(db.Float, nullable=True)
