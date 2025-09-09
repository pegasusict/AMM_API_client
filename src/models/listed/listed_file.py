from pydantic import BaseModel


class ListedFile(BaseModel):
    """Lightweight File model used in paginated listings."""

    id: int
    path: str
    fileName: str
    fileType: str
    size: int
    codec: str | None = None
    bitrate: int | None = None
    duration: int | None = None
    stage: str
