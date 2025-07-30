from .base import GenreBaseService
from models.genre import Genre


class GenreReadService(GenreBaseService):
    async def get_paginated(self, limit: int, offset: int) -> list[Genre]:
        result = await self._exec("get_paginated", "paginated_genres", {"limit": limit, "offset": offset})
        return [Genre(**a) for a in result["genres"]]

    async def search(self, query_str: str, limit: int) -> list[Genre]:
        result = await self._exec("search_genres", "search_genres", {"query": query_str, "limit": limit})
        return [Genre(**a) for a in result["searchGenres"]]
