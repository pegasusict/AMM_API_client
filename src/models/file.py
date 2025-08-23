from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class File:
    """Represents a media file stored in the system."""

    id: int
    filename: str
    filepath: str
    filesize: int  # in bytes
    mimetype: Optional[str] = None
    duration: Optional[float] = None  # in seconds
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
