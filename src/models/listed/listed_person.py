from pydantic import BaseModel
from typing import Optional


class ListedPerson(BaseModel):
    id: int
    full_name: str
    alias: Optional[str] = None
    nick_name: Optional[str] = None
