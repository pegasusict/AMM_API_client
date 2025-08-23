# services/stat_service.py
from .base_service import BaseService
from models.stat import Stat


class StatService(BaseService):
    async def get_all(self) -> list[Stat]:
        result = await self._exec("stats", "stats.graphql", {})
        return [Stat(**item) for item in result["stats"]]
