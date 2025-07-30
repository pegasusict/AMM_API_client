from .base import LabelBaseService
from models.label import Label


class LabelReadService(LabelBaseService):
    async def get_paginated(self, limit: int, offset: int) -> list[Label]:
        result = await self._exec("get_paginated", "paginated_labels", {"limit": limit, "offset": offset})
        return [Label(**a) for a in result["labels"]]

    async def search(self, query_str: str, limit: int) -> list[Label]:
        result = await self._exec("search_labels", "search_labels", {"query": query_str, "limit": limit})
        return [Label(**a) for a in result["searchLabels"]]
