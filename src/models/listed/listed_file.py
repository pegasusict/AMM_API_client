from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ListedFile(BaseModel):
    """Lightweight model for representing files in lists/pagination."""

    id: int
    file_name: Optional[str] = None
    file_type: Optional[str] = None
    file_extension: Optional[str] = None
    size: Optional[int] = None
    duration: Optional[int] = None
    imported: Optional[datetime] = None
    processed: Optional[datetime] = None
