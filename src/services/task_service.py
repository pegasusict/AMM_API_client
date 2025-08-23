from typing import Optional
from client import AMMGraphQLClient
from .base_service import BaseService
from models import (
    DisplayTask,
    TaskStats,
    TaskStatTrend,
    TaskStatSummary,
)
from gql import (
    DISPLAY_TASKS,
    TASK_STATS,
    TASK_STAT_TREND,
    TASK_STAT_SUMMARY,
)


class TaskService(BaseService):
    """Service for fetching task information and statistics."""

    def __init__(self, gql: AMMGraphQLClient):
        super().__init__(gql)

    async def get_display_tasks(self) -> list[DisplayTask]:
        """Fetch a list of tasks."""
        result = await self._exec("list_tasks", DISPLAY_TASKS)
        return [DisplayTask(**item) for item in result["getTaskDisplay"]]

    async def get_task_stats(self, task_type: str) -> Optional[TaskStats]:
        """Fetch aggregated statistics for a task type."""
        result = await self._exec("task_stats", TASK_STATS, {"taskType": task_type})
        stats = result.get("taskStats")
        return TaskStats(**stats) if stats else None

    async def get_task_stat_trend(self, task_type: str) -> Optional[TaskStatTrend]:
        """Fetch timeseries trend for a task type."""
        result = await self._exec("task_stat_trend", TASK_STAT_TREND, {"taskType": task_type})
        trend = result.get("taskStatTrend")
        return TaskStatTrend(**trend) if trend else None

    async def get_task_stat_summary(self, task_type: str) -> Optional[TaskStatSummary]:
        """Fetch delta-based summary stats for a task type."""
        result = await self._exec("task_stat_summary", TASK_STAT_SUMMARY, {"taskType": task_type})
        summary = result.get("taskStatSummary")
        return TaskStatSummary(**summary) if summary else None
