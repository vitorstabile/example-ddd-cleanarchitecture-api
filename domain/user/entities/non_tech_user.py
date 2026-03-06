from dataclasses import dataclass

from app.domain.user.entities.base_user import User


@dataclass
class NonTechUser(User):
    department: str
