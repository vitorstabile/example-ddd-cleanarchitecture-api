from abc import ABC, abstractmethod
from app.domain.user.entities.base_user import User


class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass
