from services.base_crud import CRUDService
from models.genre import Genre


class GenreService(CRUDService):
    def __init__(self, gql):
        super().__init__(gql, Genre)

    async def get_paginated(self, limit: int = 10, offset: int = 0):
        return await super().paginate("paginated_genres", "genres", limit, offset)

    async def search(self, query: str, limit: int = 10):  # type: ignore
        return await super().search("search_genres", "searchGenres", query, limit)

    async def update(self, genre_id: int, **fields):  # type: ignore
        return await super().update("update_genre", "genre", genre_id, **fields)

    async def delete(self, genre_id: int):  # type: ignore
        return await super().delete("delete_genre", "genre", genre_id)
