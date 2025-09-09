from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class Track(BaseModel):
    id: Optional[int]
    title: Optional[str]
    title_sort: Optional[str]
    subtitle: Optional[str]
    artists: Optional[List[int]]
    albums: Optional[List[int]]
    key: Optional[str]
    genres: Optional[List[int]]
    mbid: Optional[str]
    conductors: Optional[List[int]]
    composers: Optional[List[int]]
    lyricists: Optional[List[int]]
    producers: Optional[List[int]]
    releasedate: Optional[date]
    lyrics: Optional[str]
    files: Optional[List[int]]
    task_id: Optional[int]
