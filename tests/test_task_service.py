import pytest
from services import TaskService, StatService
from models import DisplayTask, TaskStats, TaskStatSummary, TaskStatTrend


@pytest.mark.asyncio
async def test_tasks(gql_client):
    service = TaskService(gql_client)
    tasks = await service.tasks()
    assert all(isinstance(t, DisplayTask) for t in tasks)


@pytest.mark.asyncio
async def test_task_stats(gql_client):
    service = TaskService(gql_client)
    stats = await service.task_stats("IMPORT")
    assert isinstance(stats, TaskStats)
    assert stats.imported == 100


@pytest.mark.asyncio
async def test_task_stat_trend(gql_client):
    service = TaskService(gql_client)
    trend = await service.task_stat_trend("IMPORT")
    assert isinstance(trend, TaskStatTrend)


@pytest.mark.asyncio
async def test_task_stat_summary(gql_client):
    service = TaskService(gql_client)
    summary = await service.task_stat_summary("IMPORT")
    assert isinstance(summary, TaskStatSummary)
    assert summary.imported.value == 10
