from models import DisplayTask, TaskStats, TaskStatSummary, TaskStatTrend
from .base_service import BaseService
from gql import TASKS, DISPLAY_TASKS, TASK_STATS, TASK_STAT_SUMMARY, TASK_STAT_TREND


class TaskService(BaseService):
    """Service for querying background tasks and statistics."""

    async def get_tasks(self) -> list[DisplayTask]:
        result = await self._exec("tasks", TASKS)
        return [DisplayTask(**t) for t in result["tasks"]]

    async def get_display_tasks(self) -> list[DisplayTask]:
        result = await self._exec("display_tasks", DISPLAY_TASKS)
        return [DisplayTask(**t) for t in result["getTaskDisplay"]]

    async def get_task_stats(self, task_type: str) -> TaskStats:
        result = await self._exec("task_stats", TASK_STATS, {"taskType": task_type})
        return TaskStats(**result["taskStats"])

    async def get_task_stat_summary(self, task_type: str) -> TaskStatSummary:
        result = await self._exec("task_stat_summary", TASK_STAT_SUMMARY, {"taskType": task_type})
        return TaskStatSummary(**result["taskStatSummary"])

    async def get_task_stat_trend(self, task_type: str) -> TaskStatTrend:
        result = await self._exec("task_stat_trend", TASK_STAT_TREND, {"taskType": task_type})
        return TaskStatTrend(**result["taskStatTrend"])
