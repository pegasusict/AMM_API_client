from pydantic import BaseModel
from typing import Optional, List


class ListedTrack(BaseModel):
    id: int
    title: str
    subtitle: Optional[str] = None
    artists: Optional[List[int]] = None
