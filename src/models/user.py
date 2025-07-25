from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str
    name: str


class PlaybackState(BaseModel):
    current_track_id: str | None
    position: int
    is_playing: bool
