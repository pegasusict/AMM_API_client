from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from .stat import StatDelta, StatPoint


class DisplayTask(BaseModel):
    """Task as shown in task lists."""

    id: int
    task_type: str
    status: str
    started: Optional[datetime] = None
    finished: Optional[datetime] = None
    progress: Optional[int] = None
    message: Optional[str] = None


class TaskStats(BaseModel):
    """Aggregated statistics for a task type."""

    task_type: str
    imported: int
    parsed: int
    trimmed: int
    deduped: int
    total_playtime: int
    total_filesize: int


class TaskStatTrend(BaseModel):
    """Timeseries trend data for a task type."""

    task_type: str
    imported: list[StatPoint]
    parsed: list[StatPoint]
    trimmed: list[StatPoint]
    deduped: list[StatPoint]
    total_playtime: list[StatPoint]
    total_filesize: list[StatPoint]


class TaskStatSummary(BaseModel):
    """Delta-based summary between two task snapshots."""

    task_type: str
    imported: StatDelta
    parsed: StatDelta
    trimmed: StatDelta
    deduped: StatDelta
    total_playtime: StatDelta
    total_filesize: StatDelta
