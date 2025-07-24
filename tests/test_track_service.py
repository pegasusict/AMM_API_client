import pytest

# import asyncio
from typing import Optional
from services.track_service import TrackService
from models.track import Track
# from client import AMMGraphQLClient


class FakeGraphQLClient:
    async def execute(self, query_str: str, variables: Optional[dict] = None) -> dict:
        return {
            "tracks": [
                {
                    "id": "1",
                    "title": "Test Track",
                    "duration": 180,
                    "album": {"id": "a1", "name": "Test Album"},
                }
            ]
        }


@pytest.mark.asyncio
async def test_get_tracks_success():
    client = FakeGraphQLClient()
    service = TrackService(client)  # type: ignore
    tracks = await service.get_tracks()

    assert isinstance(tracks, list)
    assert isinstance(tracks[0], Track)
    assert tracks[0].title == "Test Track"


@pytest.mark.asyncio
async def test_get_tracks_empty():
    class EmptyClient:
        async def execute(self, query_str: str, variables: Optional[dict] = None) -> dict:
            return {"tracks": []}

    service = TrackService(EmptyClient())  # type: ignore
    tracks = await service.get_tracks()
    assert tracks == []
