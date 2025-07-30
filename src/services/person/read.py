from .base import PersonBaseService
from models.person import Person


class PersonReadService(PersonBaseService):
    async def get_paginated(self, limit: int, offset: int) -> list[Person]:
        result = await self._exec("get_paginated", "paginated_persons", {"limit": limit, "offset": offset})
        return [Person(**p) for p in result["persons"]]

    async def search(self, query_str: str, limit: int) -> list[Person]:
        result = await self._exec("search_persons", "search_persons", {"query": query_str, "limit": limit})
        return [Person(**p) for p in result["searchPersons"]]
