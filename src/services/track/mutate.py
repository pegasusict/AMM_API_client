from models.track import Track
from .base import TrackBaseService


class TrackMutateService(TrackBaseService):
    async def update(self, track_id: int, **fields) -> Track:
        result = await self._exec("update", "update_track", {"trackId": track_id, "input": fields})
        return Track(**result["updateTrack"])

    async def delete(self, track_id: int) -> dict:
        result = await self._exec("delete", "delete_track", {"trackId": track_id})
        return result["deleteTrack"]
