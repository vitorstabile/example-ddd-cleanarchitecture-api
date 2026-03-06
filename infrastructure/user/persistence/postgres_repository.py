from app.application.interfaces.user_repository import IUserRepository
from app.domain.user.entities.base_user import User


class PostgresUserRepository(IUserRepository):
    def save(self, user: User):
        print(f"--- Logic for PostgreSQL: Saving {user.username} ---")