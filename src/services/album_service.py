from services.base_crud import CRUDService
from models.album import Album


class AlbumService(CRUDService):
    def __init__(self, gql):
        super().__init__(gql, Album)

    async def get_paginated(self, limit: int = 10, offset: int = 0):
        return await super().paginate("paginated_albums", "albums", limit, offset)

    async def search(self, query: str, limit: int = 10):  # type: ignore
        return await super().search("search_albums", "searchAlbums", query, limit)

    async def update(self, album_id: int, **fields):  # type: ignore
        return await super().update("update_album", "album", album_id, **fields)

    async def delete(self, album_id: int):  # type: ignore
        return await super().delete("delete_album", "album", album_id)
