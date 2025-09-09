# models/playback_state.py
from pydantic import BaseModel
from typing import Optional, List


class PlaybackTrack(BaseModel):
    id: int
    title: str
    subtitle: Optional[str] = None
    artists: List[str]
    album_picture: Optional[str] = None
    duration_seconds: Optional[int] = None
    lyrics: Optional[str] = None


class PlaybackState(BaseModel):
    current_track: Optional[PlaybackTrack] = None
    is_playing: bool
