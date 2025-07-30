from .base import AlbumBaseService
from models.album import Album


class AlbumMutateService(AlbumBaseService):
    async def update(self, album_id: int, **kwargs) -> Album:
        result = await self._exec("update_album", "update_album", {"albumId": album_id, "input": kwargs})
        return Album(**result["updateAlbum"])

    async def delete(self, album_id: int) -> dict:
        result = await self._exec("delete_album", "delete_album", {"albumId": album_id})
        return result["deleteAlbum"]
