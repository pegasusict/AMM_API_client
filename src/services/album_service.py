from client import AMMGraphQLClient
from utils.graphql_helpers import load_query
from models.album import Album


class AlbumService:
    def __init__(self, gql: AMMGraphQLClient):
        self.gql = gql

    async def get_paginated(self, limit: int = 10, offset: int = 0) -> list[Album]:
        query = load_query("paginated_albums")
        result = await self.gql.execute(query, {"limit": limit, "offset": offset})
        return [Album(**a) for a in result["albums"]]

    async def search(self, query_str: str, limit: int = 10) -> list[Album]:
        query = load_query("search_albums")
        result = await self.gql.execute(query, {"query": query_str, "limit": limit})
        return [Album(**a) for a in result["searchAlbums"]]

    async def update(self, album_id: int, **kwargs) -> Album:
        """Edit album fields by ID."""
        query = load_query("update_album")
        result = await self.gql.execute(query, {"albumId": album_id, "input": kwargs})
        return Album(**result["updateAlbum"])

    async def delete(self, album_id: int) -> dict:
        """Delete album by ID. Returns { success, message }."""
        query = load_query("delete_album")
        result = await self.gql.execute(query, {"albumId": album_id})
        return result["deleteAlbum"]
