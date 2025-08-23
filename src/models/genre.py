from pydantic import BaseModel
from typing import Optional, List, Generic, TypeVar
from datetime import date, datetime


class Genre(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    albums: Optional[List[int]]
    tracks: Optional[List[int]]
    parents: Optional[List[int]]
    children: Optional[List[int]]
