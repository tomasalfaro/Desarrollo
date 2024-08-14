import unittest
from app.models import Workout
from app.repositories import WorkoutRepository, UserRepository
from app import create_app, db

class TestworkoutRepository(unittest.TestCase):

    def setUp(self):
        self.repository = WorkoutRepository()
        self.repository_1 = UserRepository()
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def test_save_workout(self):
        workout = Workout(name_workout="leg day",date_time='2022-04-25 10:00:00', user_id=self.repository_1.find_by_username("test_user_2").id)
        saved_workout = self.repository.save(workout)
        self.assertIsNotNone(saved_workout.id)

    def test_find_workout(self):
        workout = Workout(name_workout="pecho day",date_time='2022-04-25 10:00:00', user_id=self.repository_1.find_by_username("test_user_2").id)
        saved_workout = self.repository.save(workout)
        found_workout = self.repository.find(saved_workout.id)
        self.assertEqual(found_workout.id, saved_workout.id)
        self.assertEqual(found_workout.name_workout, saved_workout.name_workout)
        self.assertEqual(found_workout.user_id, saved_workout.user_id)

    def test_update_workout(self):
        workout = Workout(name_workout="back day",date_time='2022-04-25 10:00:00', user_id=self.repository_1.find_by_username("test_user_2").id)
        saved_workout = self.repository.save(workout)
        saved_workout.date_time = "2022-04-25 11:00:00"
        updated_workout = self.repository.update(saved_workout, saved_workout.id)
        self.assertEqual(updated_workout.date_time.isoformat(), "2022-04-25T11:00:00")

    def test_delete_workout(self):
        workout = Workout(name_workout="chest day",date_time='2022-04-26 10:00:00', user_id=self.repository_1.find_by_username("test_user_2").id)
        saved_workout = self.repository.save(workout)
        self.repository.delete(saved_workout)
        deleted_workout = self.repository.find(saved_workout.id)
        self.assertIsNone(deleted_workout)

if __name__ == '__main__':
    unittest.main()
