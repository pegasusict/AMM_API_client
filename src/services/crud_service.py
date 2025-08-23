from typing import Any, Type, TypeVar

from client import AMMGraphQLClient
from .base_service import BaseService

ListModelT = TypeVar("ListModelT")
DetailModelT = TypeVar("DetailModelT")


class CRUDService(BaseService):
    """Base service for CRUD operations with optional separate list and detail models."""

    def __init__(self, gql: AMMGraphQLClient, list_model: Type[ListModelT], detail_model: Type[DetailModelT] = None):  # type: ignore
        self.gql = gql
        self.list_model = list_model
        self.detail_model = detail_model or list_model  # fallback to same model if only one is given

    async def update(self, file: str, object_key: str, object_id: int, **fields) -> DetailModelT:  # type: ignore
        """Update an object with given fields."""
        result = await self._exec("update", file, {"input": fields, f"{object_key}Id": object_id})
        return self.detail_model(**result[f"update{object_key.capitalize()}"])  # type: ignore

    async def delete(self, file: str, object_key: str, object_id: int) -> dict[str, Any]:
        """Delete an object by ID."""
        result = await self._exec("delete", file, {f"{object_key}Id": object_id})
        return result[f"delete{object_key.capitalize()}"]

    async def search(self, file: str, result_key: str, query: str, limit: int) -> list[ListModelT]:  # type: ignore
        """Search for objects by query."""
        result = await self._exec("search", file, {"query": query, "limit": limit})
        return [self.list_model(**item) for item in result[result_key]]  # type: ignore

    async def paginate_with_total(self, file: str, result_key: str, limit: int, offset: int) -> tuple[list[ListModelT], int]:  # type: ignore
        """Paginate objects with total count."""
        result = await self._exec("paginate", file, {"limit": limit, "offset": offset})
        items = [self.list_model(**item) for item in result[result_key]["items"]]
        total = result[result_key]["total"]
        return items, total  # type: ignore
