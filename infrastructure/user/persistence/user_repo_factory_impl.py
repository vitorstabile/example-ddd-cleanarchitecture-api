# app/infrastructure/user/persistence/user_repo_factory_impl.py
from app.application.interfaces.user_repo_factory import IUserRepoFactory
from app.infrastructure.user.persistence.postgres_repository import PostgresUserRepository
from app.infrastructure.user.persistence.mongodb_repository import MongoUserRepository


class UserRepoFactoryImpl(IUserRepoFactory):
    def __init__(self):
        self._repos = {
            "postgres": PostgresUserRepository(),
            "mongo": MongoUserRepository()
        }

    def get_repository(self, target: str):
        repo = self._repos.get(target.lower())
        if not repo:
            raise ValueError(f"Database {target} not supported.")
        return repo
