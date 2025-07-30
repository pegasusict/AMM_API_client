from client import AMMGraphQLClient
from utils.graphql_helpers import load_query
from errors import GraphQLClientError


class PersonBaseService:
    def __init__(self, gql: AMMGraphQLClient):
        self.gql = gql

    async def _exec(self, operation: str, file: str, variables: dict):
        query = load_query(file)
        try:
            return await self.gql.execute(query, variables)
        except Exception as e:
            raise GraphQLClientError(f"{operation} failed", operation, e) from e
