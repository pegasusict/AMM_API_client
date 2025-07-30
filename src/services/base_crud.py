from client import AMMGraphQLClient
from utils.graphql_helpers import load_query
from errors import GraphQLClientError
from typing import Type, TypeVar

ModelT = TypeVar("ModelT")


class CRUDService:
    def __init__(self, gql: AMMGraphQLClient, model: Type[ModelT]):
        self.gql = gql
        self.model = model

    async def _exec(self, operation: str, file: str, variables: dict) -> dict:
        try:
            query = load_query(file)
            return await self.gql.execute(query, variables)
        except Exception as e:
            raise GraphQLClientError(f"{operation} failed", operation, e) from e

    async def update(self, file: str, object_key: str, object_id: int, **fields) -> ModelT:  # type: ignore
        result = await self._exec("update", file, {"input": fields, f"{object_key}Id": object_id})
        return self.model(**result[f"update{object_key.capitalize()}"])  # type: ignore

    async def delete(self, file: str, object_key: str, object_id: int) -> dict:
        result = await self._exec("delete", file, {f"{object_key}Id": object_id})
        return result[f"delete{object_key.capitalize()}"]

    async def search(self, file: str, result_key: str, query: str, limit: int) -> list[ModelT]:  # type: ignore
        result = await self._exec("search", file, {"query": query, "limit": limit})
        return [self.model(**item) for item in result[result_key]]  # type: ignore

    async def paginate(self, file: str, result_key: str, limit: int, offset: int) -> list[ModelT]:  # type: ignore
        result = await self._exec("paginate", file, {"limit": limit, "offset": offset})
        return [self.model(**item) for item in result[result_key]]  # type: ignore
