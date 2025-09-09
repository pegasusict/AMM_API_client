# models/player_queue.py
from pydantic import BaseModel
from typing import List, Optional

from .player import PlayerTrack


class PlayerQueue(BaseModel):
    id: Optional[int] = None
    tracks: List[PlayerTrack] = []
