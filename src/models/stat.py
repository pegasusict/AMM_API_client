from pydantic import BaseModel
from typing import Optional


class Stat(BaseModel):
    id: Optional[int]
    name: Optional[str]
    value: Optional[float]
    range_start: Optional[float]
    range_end: Optional[float]
    unit: Optional[str]
