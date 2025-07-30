from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Label(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    founded: Optional[datetime]
    defunct: Optional[datetime]
