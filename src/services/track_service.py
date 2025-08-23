from services.crud_service import CRUDService
from models.track import Track
from models.listed.listed_track import ListedTrack


class TrackService(CRUDService):
    def __init__(self, gql):
        super().__init__(gql, list_model=ListedTrack, detail_model=Track)

    async def get(self, track_id: int) -> Track:
        result = await self._exec("get", "get_track.graphql", {"trackId": track_id})
        return self.detail_model(**result["track"])  # type: ignore

    async def update_track(self, track_id: int, **fields) -> Track:
        return await self.update("update_track.graphql", "track", track_id, **fields)

    async def delete_track(self, track_id: int):
        return await self.delete("delete_track.graphql", "track", track_id)

    async def search_tracks(self, query: str, limit: int = 10):
        return await self.search("search_tracks.graphql", "searchTracks", query, limit)

    async def paginate_tracks(self, limit: int, offset: int):
        return await self.paginate_with_total("paginated_tracks.graphql", "paginatedTracks", limit, offset)
