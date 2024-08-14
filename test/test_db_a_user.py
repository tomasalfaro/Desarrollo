import unittest
from app.models import User
from app.repositories import UserRepository
from app import create_app, db

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.repository = UserRepository()
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def test_save_user(self):
        user = User(username="test_user_1",password="123456", email="test_0@example.com")
        saved_user = self.repository.save(user)
        self.assertIsNotNone(saved_user.id)

    def test_find_user(self):
        user = User(username="test_user_2",password="123456",email="test_1@example.com")
        saved_user = self.repository.save(user)
        found_user = self.repository.find(saved_user.id)
        self.assertEqual(found_user.id, saved_user.id)
        self.assertEqual(found_user.username, saved_user.username)
        self.assertEqual(found_user.email, saved_user.email)

    def test_update_user(self):
        user = User(username="test_user_3", password="123456",email="test_2@example.com")
        saved_user = self.repository.save(user)
        saved_user.email = "updated_test_2@example.com"
        updated_user = self.repository.update(saved_user, saved_user.id)
        self.assertEqual(updated_user.email, "updated_test_2@example.com")

    def test_delete_user(self):
        user = User(username="test_user_4", password="123456",email="test_3@example.com")
        saved_user = self.repository.save(user)
        self.repository.delete(saved_user)
        deleted_user = self.repository.find(saved_user.id)
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
