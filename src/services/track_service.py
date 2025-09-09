from models import Track, ListedTrack
from .crud_service import CRUDService
from gql import (
    GET_TRACK,
    UPDATE_TRACK,
    DELETE_TRACK,
    SEARCH_TRACKS,
    PAGINATED_TRACKS,
)


class TrackService(CRUDService):
    """Service for managing tracks."""

    def __init__(self, gql_client):
        super().__init__(gql_client, list_model=ListedTrack, detail_model=Track)

    async def get(self, track_id: int) -> Track:
        result = await self._exec("get_track", GET_TRACK, {"trackId": track_id})
        return Track(**result["getTrack"])

    async def update_track(self, track_id: int, **fields) -> Track:
        return await self.update(UPDATE_TRACK, "track", track_id, **fields)

    async def delete_track(self, track_id: int) -> bool:
        return await self.delete(DELETE_TRACK, "track", track_id)  # type: ignore

    async def search_tracks(self, query: str, limit: int = 10) -> list[ListedTrack]:
        return await self.search(SEARCH_TRACKS, "searchTracks", query, limit)

    async def paginate_tracks(self, limit: int = 10, offset: int = 0):
        return await self.paginate_with_total(PAGINATED_TRACKS, "paginatedTracks", limit, offset)
