import unittest
from app.models import Repetition
from app.repositories import ExcerciseRepository,WorkoutRepository, RepetitionRepository
from app import create_app, db

class TestrepetitionRepository(unittest.TestCase):

    def setUp(self):
        self.repository = RepetitionRepository()
        self.repository_1 = ExcerciseRepository()
        self.repository_2 = WorkoutRepository()
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def test_save_repetition(self):
        repetition = Repetition(workout_id=self.repository_2.find_by_name_workout("pecho day").id , excercise_id=self.repository_1.find_by_name("press plano").id , series_number=3,num_repetitions=[10,9,11],peso=50)
        saved_repetition = self.repository.save(repetition)
        self.assertIsNotNone(saved_repetition.id)

    def test_find_repetition(self):
        repetition = Repetition(workout_id=self.repository_2.find_by_name_workout("pecho day").id , excercise_id=self.repository_1.find_by_name("press inclinado").id , series_number=3,num_repetitions=[10,9,11],peso=50)
        saved_repetition = self.repository.save(repetition)
        found_repetition = self.repository.find(saved_repetition.id)
        self.assertEqual(found_repetition.id, saved_repetition.id)
        
    def test_update_repetition(self):
        repetition = Repetition(workout_id=self.repository_2.find_by_name_workout("pecho day").id , excercise_id=self.repository_1.find_by_name("press inclinado").id , series_number=3,num_repetitions=[10,9,11],peso=50)
        saved_repetition = self.repository.save(repetition)
        saved_repetition.num_repetitions = [11,10,9]
        updated_repetition = self.repository.update(saved_repetition, saved_repetition.id)
        self.assertEqual(updated_repetition.num_repetitions, [11,10,9])

    def test_delete_repetition(self):
        repetition = Repetition(workout_id=self.repository_2.find_by_name_workout("pecho day").id , excercise_id=self.repository_1.find_by_name("press inclinado").id , series_number=3,num_repetitions=[12,12,12],peso=60)
        saved_repetition = self.repository.save(repetition)
        self.repository.delete(saved_repetition)
        deleted_repetition = self.repository.find(saved_repetition.id)
        self.assertIsNone(deleted_repetition)

    def test_find_repetition_by_excercise(self):
        excercise_id=self.repository_1.find_by_name("press inclinado").id        
        repetitions = self.repository.find_by_exercise(excercise_id)
        print(repetitions)
        self.assertIsNotNone(repetitions)

if __name__ == '__main__':
    unittest.main()
