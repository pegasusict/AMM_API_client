from pydantic import BaseModel
from typing import Optional, List, Generic, TypeVar
from datetime import date, datetime


class Person(BaseModel):
    id: Optional[int]
    mbid: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    full_name: Optional[str]
    alias: Optional[str]
    nick_name: Optional[str]
    sort_name: Optional[str]
    date_of_birth: Optional[date]
    date_of_death: Optional[date]
    picture: Optional[str]
    performed_tracks: Optional[List[int]]
    conducted_tracks: Optional[List[int]]
    composed_tracks: Optional[List[int]]
    lyric_tracks: Optional[List[int]]
    produced_tracks: Optional[List[int]]
    performed_albums: Optional[List[int]]
    conducted_albums: Optional[List[int]]
    composed_albums: Optional[List[int]]
    lyric_albums: Optional[List[int]]
    produced_albums: Optional[List[int]]
    task_id: Optional[int]
    labels: Optional[List[int]]
