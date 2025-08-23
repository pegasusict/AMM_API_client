# models/playlist_models.py
from typing import List, Optional
from pydantic import BaseModel


class Playlist(BaseModel):
    id: int
    name: str
    track_ids: List[int]


class PlayerTrack(BaseModel):
    id: int
    title: str
    subtitle: Optional[str]
    artists: List[str]
    album_picture: Optional[str]
    duration_seconds: Optional[int]
    lyrics: Optional[str] = None
