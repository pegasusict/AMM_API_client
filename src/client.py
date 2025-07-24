from typing import Optional
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from errors import GraphQLClientError


class AMMGraphQLClient:
    def __init__(self, token: str, endpoint: str):
        self.token = token
        self.endpoint = endpoint
        self.transport = AIOHTTPTransport(url=endpoint, headers={"Authorization": f"Bearer {token}"})
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    async def execute(self, query_str: str, variables: Optional[dict] = None) -> dict:
        try:
            async with self.client as session:
                query = gql(query_str)
                return await session.execute(query, variable_values=variables or {})
        except Exception as e:
            raise GraphQLClientError("GraphQL query failed", operation="execute", original_error=e) from e
