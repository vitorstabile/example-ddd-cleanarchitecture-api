from app.domain.user.entities.base_user import User
from app.domain.user.entities.tech_user import TechUser
from app.domain.user.entities.non_tech_user import NonTechUser


class UserFactory:
    @staticmethod
    def create(user_type: str, data: dict) -> User:
        if user_type == "tech":
            return TechUser(id=data["id"], username=data["username"], git_handle=data["git_handle"])
        return NonTechUser(id=data["id"], username=data["username"], department=data["department"])
