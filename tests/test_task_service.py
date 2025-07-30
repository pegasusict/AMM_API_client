import pytest
from services.track_service import TrackService
from models.track import Track


class FakeTrackClient:
    async def execute(self, query, variables=None):
        if "updateTrack" in query:
            return {
                "updateTrack": {
                    "id": variables["trackId"],  # type: ignore
                    "title": variables["input"].get("title", "Untitled"),  # type: ignore
                    "subtitle": variables["input"].get("subtitle", ""),  # type: ignore
                    "duration": 180,
                    "releasedate": "2020-01-01",
                    "key": "C",
                    "genres": [1, 2],
                }
            }
        elif "deleteTrack" in query:
            return {"deleteTrack": {"success": True, "message": "Track deleted"}}
        elif "tracks(" in query:
            return {"tracks": [{"id": 1, "title": "Sample", "duration": 180}]}
        return {}


@pytest.mark.asyncio
async def test_update_track():
    service = TrackService(FakeTrackClient())  # type: ignore
    updated = await service.update(track_id=1, title="Edited")
    assert isinstance(updated, Track)
    assert updated.title == "Edited"
    assert updated.key == "C"


@pytest.mark.asyncio
async def test_delete_track():
    service = TrackService(FakeTrackClient())  # type: ignore
    result = await service.delete(track_id=1)
    assert result["success"]
    assert result["message"] == "Track deleted"
