from models import Album, ListedAlbum
from .crud_service import CRUDService
from gql import (
    GET_ALBUM,
    UPDATE_ALBUM,
    DELETE_ALBUM,
    SEARCH_ALBUMS,
    PAGINATED_ALBUMS,
)


class AlbumService(CRUDService):
    """Service for managing albums."""

    def __init__(self, gql_client):
        super().__init__(gql_client, list_model=ListedAlbum, detail_model=Album)

    async def get_album(self, album_id: int) -> Album:
        result = await self._exec("get_album", GET_ALBUM, {"albumId": album_id})
        return Album(**result["getAlbum"])

    async def update_album(self, album_id: int, **fields) -> Album:
        return await self.update(UPDATE_ALBUM, "album", album_id, **fields)

    async def delete_album(self, album_id: int) -> bool:
        return await self.delete(DELETE_ALBUM, "album", album_id)  # type: ignore

    async def search_albums(self, query: str, limit: int = 10) -> list[ListedAlbum]:
        return await self.search(SEARCH_ALBUMS, "searchAlbums", query, limit)

    async def paginate_albums(self, limit: int = 10, offset: int = 0):
        return await self.paginate_with_total(PAGINATED_ALBUMS, "paginatedAlbums", limit, offset)
