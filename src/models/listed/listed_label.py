from pydantic import BaseModel
from typing import Optional


class ListedLabel(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
