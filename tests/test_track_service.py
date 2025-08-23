import pytest
from services import TrackService
from models import Track, ListedTrack


@pytest.mark.asyncio
async def test_get_track(gql_client):
    service = TrackService(gql_client)
    track = await service.get(42)
    assert isinstance(track, Track)
    assert track.title == "Mock Track"


@pytest.mark.asyncio
async def test_update_track(gql_client):
    service = TrackService(gql_client)
    track = await service.update_track(42, title="Updated Track")
    assert track.title == "Updated Track"


@pytest.mark.asyncio
async def test_delete_track(gql_client):
    service = TrackService(gql_client)
    result = await service.delete_track(42)
    assert result["success"]


@pytest.mark.asyncio
async def test_search_tracks(gql_client):
    service = TrackService(gql_client)
    results = await service.search_tracks("Query", 5)
    assert all(isinstance(item, ListedTrack) for item in results)
    assert len(results) == 2


@pytest.mark.asyncio
async def test_paginate_tracks(gql_client):
    service = TrackService(gql_client)
    items, total = await service.paginate_tracks(10, 0)
    assert len(items) == 1
    assert total == 1
