from pydantic import BaseModel
from typing import Optional


class ListedGenre(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
