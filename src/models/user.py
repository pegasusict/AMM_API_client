from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str
    name: str


class PlaybackState(BaseModel):
    currentTrackId: str | None
    position: int
    isPlaying: bool
