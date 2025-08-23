from datetime import datetime
from pydantic import BaseModel


class StatPoint(BaseModel):
    """Single datapoint in a trend line."""

    timestamp: datetime
    value: int


class StatDelta(BaseModel):
    """Change between two stat snapshots."""

    value: int
    change: int
    percentage: float
