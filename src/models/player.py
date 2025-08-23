from pydantic import BaseModel
from typing import Optional, List


class PlayerTrack(BaseModel):
    id: int
    title: str
    subtitle: Optional[str] = None
    artists: List[str]
    album_picture: Optional[str] = None
    duration_seconds: Optional[int] = None
    lyrics: Optional[str] = None


class PlayerStatus(BaseModel):
    current_track: Optional[PlayerTrack]
    is_playing: bool
