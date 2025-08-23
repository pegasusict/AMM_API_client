from typing import Optional
from pydantic import BaseModel


class ListedUser(BaseModel):
    id: int
    username: Optional[str]
    email: Optional[str]
    role: Optional[str]
