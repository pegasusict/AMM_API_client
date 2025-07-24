from client import AMMGraphQLClient
from models.user import User, PlaybackState
from utils.graphql_helpers import load_query
from errors import GraphQLClientError


class UserService:
    def __init__(self, gql: AMMGraphQLClient):
        self.gql = gql
        self.query_me = load_query("me")
        self.query_playback = load_query("playback_state")

    async def get_me(self) -> User:
        try:
            result = await self.gql.execute(self.query_me)
            return User(**result["me"])
        except Exception as e:
            raise GraphQLClientError("Failed to fetch user", "get_me", e) from e

    async def get_playback_state(self) -> PlaybackState:
        try:
            result = await self.gql.execute(self.query_playback)
            return PlaybackState(**result["playbackState"])
        except Exception as e:
            raise GraphQLClientError("Failed to fetch playback state", "get_playback_state", e) from e
