from typing import List
from app.models import Workout
from app.repositories import WorkoutRepository

repository = WorkoutRepository()

class WorkoutService:
    """ Clase que se encarga de CRUD de workouts """
    
    def save(self, workout: Workout) -> Workout:
        # Guarda un nuevo entrenamiento en la base de datos
        return repository.save(workout)
    
    def update(self, workout: Workout, id: int) -> Workout:
        # Actualiza un entrenamiento existente por su ID
        return repository.update(workout, id)
    
    def delete(self, workout: Workout) -> None:
        # Elimina un entrenamiento de la base de datos
        repository.delete(workout)
    
    def all(self) -> List[Workout]:
        # Devuelve una lista con todos los entrenamientos
        return repository.all()
    
    def find(self, id: int) -> Workout:
        # Encuentra un entrenamiento por su ID
        return repository.find(id)
    
    def find_by_name_workout():
        pass