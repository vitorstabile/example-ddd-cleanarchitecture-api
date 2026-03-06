from pydantic import BaseModel, Field
from typing import Optional


class UserCreateRequest(BaseModel):
    id: str
    username: str
    user_type: str
    target_database: str = Field(..., pattern="^(postgres|mongo)$")
    git_handle: Optional[str] = None
    department: Optional[str] = None
