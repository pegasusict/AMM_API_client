from models import Genre, ListedGenre
from .crud_service import CRUDService
from gql import (
    GET_GENRE,
    UPDATE_GENRE,
    DELETE_GENRE,
    PAGINATED_GENRES,
)


class GenreService(CRUDService):
    """Service for managing genres."""

    def __init__(self, gql_client):
        super().__init__(gql_client, list_model=ListedGenre, detail_model=Genre)

    async def get_genre(self, genre_id: int) -> Genre:
        result = await self._exec("get_genre", GET_GENRE, {"genreId": genre_id})
        return Genre(**result["getGenre"])

    async def update_genre(self, genre_id: int, **fields) -> Genre:
        return await self.update(UPDATE_GENRE, "genre", genre_id, **fields)

    async def delete_genre(self, genre_id: int) -> bool:
        return await self.delete(DELETE_GENRE, "genre", genre_id)  # type: ignore

    async def paginate_genres(self, limit: int = 10, offset: int = 0):
        return await self.paginate_with_total(PAGINATED_GENRES, "paginatedGenres", limit, offset)
