from typing import Any, AsyncGenerator
from client import AMMGraphQLClient
from utils.graphql_helpers import load_query
from errors import GraphQLClientError


class BaseService:
    """Base service for raw GraphQL queries and subscriptions (no model binding)."""

    def __init__(self, gql: AMMGraphQLClient):
        self.gql = gql

    async def _exec(self, operation: str, file: str, variables: dict = None) -> dict[str, Any]:  # type: ignore
        """Execute a GraphQL query or mutation with optional variables."""
        try:
            query = load_query(file)
            return await self.gql.execute(query, variables or {})
        except Exception as e:
            raise GraphQLClientError(f"{operation} failed", operation, e) from e

    async def _subscribe(
        self,
        operation: str,
        file: str,
        variables: dict = None,  # type: ignore
        retry_forever: bool = True,
    ) -> AsyncGenerator[dict[str, Any], None]:
        """Execute a GraphQL subscription and yield events."""
        try:
            query = load_query(file)
            async for event in self.gql.subscribe(query, variables or {}, retry_forever=retry_forever):
                yield event
        except Exception as e:
            raise GraphQLClientError(f"{operation} subscription failed", operation, e) from e
