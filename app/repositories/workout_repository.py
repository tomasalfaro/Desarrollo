from typing import List
from app.models import Workout
from app import db

class WorkoutRepository:
    """ Repository para manejar operaciones CRUD de workouts """
    def save(self, workout: Workout) -> Workout:
        db.session.add(workout)
        db.session.commit()
        return workout
    
    def update(self, workout: Workout, id: int) -> Workout:
        entity = self.find(id)
        entity.user_id = workout.user_id
        entity.date_time = workout.date_time
        entity.name_workout = workout.name_workout
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, workout: Workout) -> None:
        db.session.delete(workout)
        db.session.commit()
    
    def all(self) -> List[Workout]:
        workouts = db.session.query(Workout).all()
        return workouts
    
    def find(self, id: int) -> Workout:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Workout).filter(Workout.id == id).one()
        except:
            return None
        
    def find_by_name_workout(self, name_workout: str) -> Workout:
        return db.session.query(Workout).filter(Workout.name_workout == name_workout).one_or_none()
            