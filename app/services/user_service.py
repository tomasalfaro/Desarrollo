from typing import List
from app.models import User
from app.repositories import UserRepository
from app.services.security import SecurityManager, WerkzeugSecurity

repository = UserRepository()

class UserService:
    def __init__(self) -> None:
        self.__security = SecurityManager(WerkzeugSecurity())

    def save(self, user: User) -> User:
        user.password = self.__security.generate_password(user.password)
        return repository.save(user)
    
    def update(self, user: User, id: int) -> User:
        return repository.update(user, id)
    
    def delete(self, user: User) -> None:
        repository.delete(user)
    
    def all(self) -> List[User]:
        return repository.all()
    
    def find(self, id: int) -> User:
        return repository.find(id)
    
    def find_by_username(self, username: str) -> User:
        return repository.find_by_username(username)
    
    def find_by_email(self, email: str) -> User:
        return repository.find_by_email(email)

    def check_auth(self, username: str, password: str) -> bool:
        user = self.find_by_username(username)
        if user is not None:
            return self.__security.check_password(user.password, password)
        else:
            return False
