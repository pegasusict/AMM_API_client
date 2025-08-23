from services.crud_service import CRUDService
from models.album import Album
from models.listed.listed_album import ListedAlbum


class AlbumService(CRUDService):
    def __init__(self, gql):
        super().__init__(gql, list_model=ListedAlbum, detail_model=Album)

    async def get(self, album_id: int) -> Album:
        result = await self._exec("get", "get_album.graphql", {"albumId": album_id})
        return self.detail_model(**result["album"])  # type: ignore

    async def update_album(self, album_id: int, **fields) -> Album:
        return await self.update("update_album.graphql", "album", album_id, **fields)

    async def delete_album(self, album_id: int):
        return await self.delete("delete_album.graphql", "album", album_id)

    async def search_albums(self, query: str, limit: int = 10):
        return await self.search("search_albums.graphql", "searchAlbums", query, limit)

    async def paginate_albums(self, limit: int, offset: int):
        return await self.paginate_with_total("paginated_albums.graphql", "paginatedAlbums", limit, offset)
