from pydantic import BaseModel
from typing import Optional, List, Generic, TypeVar
from datetime import date, datetime


class Label(BaseModel):
    id: Optional[int]
    name: Optional[str]
    mbid: Optional[str]
    description: Optional[str]
    founded: Optional[date]
    defunct: Optional[date]
    albums: Optional[List[int]]
    picture: Optional[str]
    parent: Optional[int]
    children: Optional[List[int]]
    owner: Optional[int]
