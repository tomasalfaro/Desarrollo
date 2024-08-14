from typing import List
from app.models import Repetition
from app import db

class RepetitionRepository:
    """ Repository para manejar operaciones CRUD de repetitions """
    def save(self, repetition: Repetition) -> Repetition:
        db.session.add(repetition)
        db.session.commit()
        return repetition
    
    def update(self, repetition: Repetition, id: int) -> Repetition:
        entity = self.find(id)
        entity.workout_id = repetition.workout_id
        entity.excercise_id = repetition.excercise_id
        entity.series_number = repetition.series_number
        entity.num_repetitions = repetition.num_repetitions
        entity.peso = repetition.peso
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, repetition: Repetition) -> None:
        db.session.delete(repetition)
        db.session.commit()
    
    def all(self) -> List[Repetition]:
        repetitions = db.session.query(Repetition).all()
        return repetitions
    
    def find(self, id: int) -> Repetition:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Repetition).filter(Repetition.id == id).one()
        except:
            return None
        
    def find_by_exercise(self, excercise_id: int) -> List[Repetition]:
        return db.session.query(Repetition).filter_by(excercise_id = excercise_id).all()