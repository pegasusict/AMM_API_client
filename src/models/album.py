from pydantic import BaseModel
from typing import Optional, List, Generic, TypeVar
from datetime import date, datetime


class Album(BaseModel):
    id: Optional[int]
    mbid: Optional[str]
    title: Optional[str]
    title_sort: Optional[str]
    subtitle: Optional[str]
    releasedate: Optional[date]
    release_country: Optional[str]
    label: Optional[str]
    tracks: Optional[List[int]]
    genres: Optional[List[int]]
    artists: Optional[List[int]]
    conductors: Optional[List[int]]
    composers: Optional[List[int]]
    lyricists: Optional[List[int]]
    producers: Optional[List[int]]
    picture: Optional[str]
    disc_count: Optional[int]
    track_count: Optional[int]
    task_id: Optional[int]
