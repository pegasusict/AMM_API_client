from .base import GenreBaseService
from models.genre import Genre


class GenreMutateService(GenreBaseService):
    async def update(self, genre_id: int, **kwargs) -> Genre:
        result = await self._exec("update_genre", "update_genre", {"genreId": genre_id, "input": kwargs})
        return Genre(**result["updateGenre"])

    async def delete(self, genre_id: int) -> dict:
        result = await self._exec("delete_genre", "delete_genre", {"genreId": genre_id})
        return result["deleteGenre"]
