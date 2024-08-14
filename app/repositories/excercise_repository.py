from typing import List
from app.models import Excercise
from app import db



class ExcerciseRepository:
    """ Repository para manejar operaciones CRUD de excercises """
    def save(self, excercise: Excercise) -> Excercise:
        db.session.add(excercise)
        db.session.commit()
        return excercise
    
    def update(self, excercise: Excercise, id: int) -> Excercise:
        entity = self.find(id)
        entity.name = excercise.name
        entity.description = excercise.description
        entity.workout_id = excercise.workout_id
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, excercise: Excercise) -> None:
        db.session.delete(excercise)
        db.session.commit()
    
    def all(self) -> List[Excercise]:
        excercises = db.session.query(Excercise).all()
        return excercises
    
    def find(self, id: int) -> Excercise:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Excercise).filter(Excercise.id == id).one()
        except:
            return None
        
    def find_by_name(self, name: str) -> Excercise:
        return db.session.query(Excercise).filter(Excercise.name == name).one_or_none()
        