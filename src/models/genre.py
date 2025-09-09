from pydantic import BaseModel
from typing import Optional, List


class Genre(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    albums: Optional[List[int]]
    tracks: Optional[List[int]]
    parents: Optional[List[int]]
    children: Optional[List[int]]
