from typing import List, Tuple
from app.models import Repetition
from app.repositories import RepetitionRepository

repository = RepetitionRepository()

class ValidationError(Exception):
    pass

class RepetitionService:
    """ Clase que se encarga de CRUD de repetitions """
    
    def save(self, repetition: Repetition) -> Repetition:
        # Guarda una nueva repetición en la base de datos
        self._validate_repetition(repetition)
        return repository.save(repetition)
    
    def _validate_repetition(self, repetition: Repetition) -> None:
        # Validar que el peso no sea negativo
        if repetition.peso < 0:
            raise ValidationError("El peso no puede ser negativo.")
        # Validar que las repeticiones no sean negativas
        if any(num < 0 for num in repetition.num_repetitions):
            raise ValidationError("Las repeticiones no pueden ser negativas.")
    def update(self, repetition: Repetition, id: int) -> Repetition:
        # Actualiza una repetición existente por su ID
        return repository.update(repetition, id)
    
    def delete(self, repetition: Repetition) -> None:
        # Elimina una repetición de la base de datos
        repository.delete(repetition)
    
    def all(self) -> List[Repetition]:
        # Devuelve una lista con todas las repeticiones
        return repository.all()
    
    def find(self, id: int) -> Repetition:
        # Encuentra una repetición por su ID
        return repository.find(id)
    
    def find_by_exercise(self, exercise_id: int) -> List[Tuple[str, float]]:
        repetitions = repository.find_by_exercise(exercise_id)
        results = [(sum(repetition.num_repetitions) / len(repetition.num_repetitions), repetition.peso) for repetition in repetitions]
        return results