from services.base_service import BaseService
from models.player import PlayerStatus


class PlayerService(BaseService):
    """Service for managing player status."""

    def __init__(self, gql):
        super().__init__(gql)

    async def get_status(self) -> PlayerStatus:
        """Fetch the current player status."""
        result = await self._exec("get_status", "get_player_status")
        return PlayerStatus(**result["getPlayerStatus"])
