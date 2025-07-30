from models.track import Track
from .base import TrackBaseService


class TrackReadService(TrackBaseService):
    async def get_tracks(self, limit: int = 10) -> list[Track]:
        result = await self._exec("get_tracks", "track", {"limit": limit})
        return [Track(**t) for t in result["tracks"]]

    async def get_paginated(self, limit: int, offset: int) -> list[Track]:
        result = await self._exec("get_tracks_paginated", "paginated_tracks", {"limit": limit, "offset": offset})
        return [Track(**t) for t in result["tracks"]]

    async def search(self, query_str: str, limit: int) -> list[Track]:
        result = await self._exec("search_tracks", "search_tracks", {"query": query_str, "limit": limit})
        return [Track(**t) for t in result["searchTracks"]]

    async def get_by_genre(self, genre_id: int, limit: int) -> list[Track]:
        result = await self._exec("tracks_by_genre", "tracks_by_genre", {"genreId": genre_id, "limit": limit})
        return [Track(**t) for t in result["tracksByGenre"]]
