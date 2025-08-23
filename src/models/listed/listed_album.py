from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class ListedAlbum(BaseModel):
    id: int
    title: str
    subtitle: Optional[str] = None
    releasedate: Optional[date] = None
    artists: Optional[List[int]] = None
