from app.application.interfaces.user_repository import IUserRepository
from app.domain.user.entities.base_user import User


class MongoUserRepository(IUserRepository):
    def save(self, user: User):
        print(f"--- Logic for MongoDB: Saving {user.username} ---")