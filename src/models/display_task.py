from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DisplayTask(BaseModel):
    task_id: Optional[str]
    task_type: Optional[str]
    progress: Optional[int]
    start_time: Optional[datetime]
    status: Optional[str]
