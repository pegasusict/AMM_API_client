from .base import AlbumBaseService
from models.album import Album


class AlbumReadService(AlbumBaseService):
    async def get_paginated(self, limit: int, offset: int) -> list[Album]:
        result = await self._exec("get_paginated", "paginated_albums", {"limit": limit, "offset": offset})
        return [Album(**a) for a in result["albums"]]

    async def search(self, query_str: str, limit: int) -> list[Album]:
        result = await self._exec("search_albums", "search_albums", {"query": query_str, "limit": limit})
        return [Album(**a) for a in result["searchAlbums"]]
