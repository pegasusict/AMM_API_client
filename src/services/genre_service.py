from services.crud_service import CRUDService
from models.genre import Genre
from models.listed.listed_genre import ListedGenre


class GenreService(CRUDService):
    def __init__(self, gql):
        super().__init__(gql, list_model=ListedGenre, detail_model=Genre)

    async def get(self, genre_id: int) -> Genre:
        result = await self._exec("get", "get_genre.graphql", {"genreId": genre_id})
        return self.detail_model(**result["genre"])  # type: ignore

    async def update_genre(self, genre_id: int, **fields) -> Genre:
        return await self.update("update_genre.graphql", "genre", genre_id, **fields)

    async def delete_genre(self, genre_id: int):
        return await self.delete("delete_genre.graphql", "genre", genre_id)

    async def paginate_genres(self, limit: int, offset: int):
        return await self.paginate_with_total("paginated_genres.graphql", "paginatedGenres", limit, offset)
