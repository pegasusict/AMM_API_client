from pydantic import BaseModel


class Album(BaseModel):
    id: str
    name: str


class Track(BaseModel):
    id: str
    title: str
    duration: int
    album: Album | None = None
    artists: list[str]
