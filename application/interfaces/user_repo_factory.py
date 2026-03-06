from abc import abstractmethod, ABC

from app.application.interfaces.user_repository import IUserRepository


class IUserRepoFactory(ABC):
    @abstractmethod
    def get_repository(self, target: str) -> IUserRepository:
        pass
