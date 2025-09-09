from datetime import datetime
from pydantic import BaseModel


class File(BaseModel):
    """Detailed File model returned by get_file query."""

    id: int
    path: str
    fileName: str
    fileType: str
    size: int
    codec: str | None = None
    bitrate: int | None = None
    duration: int | None = None
    stage: str
    createdAt: datetime
    updatedAt: datetime
