from typing import List
from app.models import Excercise
from app.repositories import ExcerciseRepository

repository = ExcerciseRepository()

class ExcerciseService:
    """ Clase que se encarga de CRUD de excercises """
    
    def save(self, excercise: Excercise) -> Excercise:
        # Guarda un nuevo ejercicio en la base de datos
        return repository.save(excercise)
    
    def update(self, excercise: Excercise, id: int) -> Excercise:
        # Actualiza un ejercicio existente por su ID
        return repository.update(excercise, id)
    
    def delete(self, excercise: Excercise) -> None:
        # Elimina un ejercicio de la base de datos
        repository.delete(excercise)
    
    def all(self) -> List[Excercise]:
        # Devuelve una lista con todos los ejercicios
        return repository.all()
    
    def find(self, id: int) -> Excercise:
        # Encuentra un ejercicio por su ID
        return repository.find(id)
