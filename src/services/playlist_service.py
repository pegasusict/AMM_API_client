# services/playlist_service.py
from .base_service import BaseService
from models.playlist_models import Playlist, PlayerTrack


class PlaylistService(BaseService):
    async def get_playlist(self, playlist_id: int) -> Playlist:
        result = await self._exec("get playlist", "get_playlist.graphql", {"playlistId": playlist_id})
        return Playlist(**result["playlist"])

    async def get_queue(self) -> list[PlayerTrack]:
        result = await self._exec("get player queue", "get_player_queue.graphql", {})
        return [PlayerTrack(**item) for item in result["playerQueue"]]
