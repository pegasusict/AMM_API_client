from typing import Any
from client import AMMGraphQLClient
from utils.graphql_helpers import load_query
from errors import GraphQLClientError


class BaseService:
    """Base service for raw GraphQL queries (read-only, no model binding)."""

    def __init__(self, gql: AMMGraphQLClient):
        self.gql = gql

    async def _exec(self, operation: str, file: str, variables: dict = None) -> dict[str, Any]:  # type: ignore
        """Execute a GraphQL operation with optional variables."""
        try:
            query = load_query(file)
            return await self.gql.execute(query, variables or {})
        except Exception as e:
            raise GraphQLClientError(f"{operation} failed", operation, e) from e
