from client import AMMGraphQLClient
from models.track import Track
from utils.graphql_helpers import load_query
from errors import GraphQLClientError


class TrackService:
    def __init__(self, gql_client: AMMGraphQLClient):
        self.gql = gql_client
        self.query = load_query("track")

    async def get_tracks(self, limit: int = 10) -> list[Track]:
        try:
            result = await self.gql.execute(self.query, {"limit": limit})
            return [Track(**track) for track in result.get("tracks", [])]
        except GraphQLClientError:
            raise

    async def get_tracks_paginated(self, limit: int = 10, offset: int = 0) -> list[Track]:
        query = load_query("paginated_tracks")
        try:
            result = await self.gql.execute(query, {"limit": limit, "offset": offset})
            return [Track(**track) for track in result["tracks"]]
        except Exception as e:
            raise GraphQLClientError("Failed to paginate tracks", "get_tracks_paginated", e) from e

    async def search_tracks(self, query_str: str, limit: int = 10) -> list[Track]:
        query = load_query("search_tracks")
        result = await self.gql.execute(query, {"query": query_str, "limit": limit})
        return [Track(**track) for track in result["searchTracks"]]

    async def get_tracks_by_genre(self, genre_id: int, limit: int = 10) -> list[Track]:
        query = load_query("tracks_by_genre")
        result = await self.gql.execute(query, {"genreId": genre_id, "limit": limit})
        return [Track(**track) for track in result["tracksByGenre"]]

    async def update(self, track_id: int, **kwargs) -> Track:
        """Update an existing track with given fields."""
        query = load_query("update_track")
        try:
            result = await self.gql.execute(query, {"trackId": track_id, "input": kwargs})
            return Track(**result["updateTrack"])
        except Exception as e:
            raise GraphQLClientError("Track update failed", "update", e) from e

    async def delete(self, track_id: int) -> dict:
        """Delete a track by ID. Returns { success, message }."""
        query = load_query("delete_track")
        try:
            result = await self.gql.execute(query, {"trackId": track_id})
            return result["deleteTrack"]
        except Exception as e:
            raise GraphQLClientError("Track deletion failed", "delete", e) from e
