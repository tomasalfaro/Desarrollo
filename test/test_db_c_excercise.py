import unittest
from app.models import Excercise
from app.repositories import ExcerciseRepository,WorkoutRepository, UserRepository
from app import create_app, db

class TestexcerciseRepository(unittest.TestCase):

    def setUp(self):
        self.repository = ExcerciseRepository()
        self.repository_1 = UserRepository()
        self.repository_2 = WorkoutRepository()
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def test_save_excercise(self):
        excercise = Excercise(name="press plano",description="press plano en pesos libres",workout_id=self.repository_2.find_by_name_workout("pecho day").id)
        saved_excercise = self.repository.save(excercise)
        self.assertIsNotNone(saved_excercise.id)

    def test_find_excercise(self):
        excercise = Excercise(name="press inclinado",description="press plano en mancuernas",workout_id=self.repository_2.find_by_name_workout("pecho day").id)
        saved_excercise = self.repository.save(excercise)
        found_excercise = self.repository.find(saved_excercise.id)
        self.assertEqual(found_excercise.id, saved_excercise.id)
        self.assertEqual(found_excercise.name, saved_excercise.name)
        self.assertEqual(found_excercise.id, saved_excercise.id)

    def test_update_excercise(self):
        excercise = Excercise(name="press declinado",description="press declinado en maquina",workout_id=self.repository_2.find_by_name_workout("pecho day").id)
        saved_excercise = self.repository.save(excercise)
        saved_excercise.description = "hecho con mancuernas"
        updated_excercise = self.repository.update(saved_excercise, saved_excercise.id)
        self.assertEqual(updated_excercise.description, "hecho con mancuernas")

    def test_delete_excercise(self):
        excercise = Excercise(name="cruce en poleas",description="con poleas de arriba",workout_id=self.repository_2.find_by_name_workout("pecho day").id)
        saved_Excercise = self.repository.save(excercise)
        self.repository.delete(saved_Excercise)
        deleted_Excercise = self.repository.find(saved_Excercise.id)
        self.assertIsNone(deleted_Excercise)

if __name__ == '__main__':
    unittest.main()
