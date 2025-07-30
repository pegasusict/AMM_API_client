from pydantic import BaseModel
from typing import Optional


class Genre(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
