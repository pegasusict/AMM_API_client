from client import AMMGraphQLClient
from models.track import Track
from utils.graphql_helpers import load_query
from errors import GraphQLClientError


class TrackService:
    def __init__(self, gql_client: AMMGraphQLClient):
        self.gql = gql_client
        self.query = load_query("track")

    async def get_tracks(self, limit: int = 10) -> list[Track]:
        try:
            result = await self.gql.execute(self.query, {"limit": limit})
            return [Track(**track) for track in result.get("tracks", [])]
        except GraphQLClientError:
            raise
