from client import AMMGraphQLClient
from utils.graphql_helpers import load_query
from models.genre import Genre


class GenreService:
    def __init__(self, gql: AMMGraphQLClient):
        self.gql = gql

    async def update(self, genre_id: int, **kwargs) -> Genre:
        query = load_query("update_genre")
        result = await self.gql.execute(query, {"genreId": genre_id, "input": kwargs})
        return Genre(**result["updateGenre"])

    async def delete(self, genre_id: int) -> dict:
        query = load_query("delete_genre")
        result = await self.gql.execute(query, {"genreId": genre_id})
        return result["deleteGenre"]
