from datetime import timezone, datetime, timedelta

from client import AMMGraphQLClient
from errors import GraphQLClientError
from utils.graphql_helpers import load_query


class SessionData:
    def __init__(self, access_token: str, expires_in: int):
        self.access_token = access_token
        self.expires_at = datetime.now(timezone.utc) + timedelta(seconds=expires_in)

    def is_expired(self) -> bool:
        return datetime.now(timezone.utc) >= self.expires_at - timedelta(seconds=30)


class AuthService:
    def __init__(self, gql: AMMGraphQLClient):
        self.gql = gql
        self.login_query = load_query("login")
        self.refresh_query = load_query("refresh")

    async def login_with_password(self, email: str, password: str) -> SessionData:
        try:
            result = await self.gql.execute(self.login_query, {"email": email, "password": password})
            token = result["login"]["access_token"]
            expires = result["login"]["expires_in"]
            return SessionData(access_token=token, expires_in=expires)
        except Exception as e:
            raise GraphQLClientError("Login failed", "login_with_password", e) from e

    async def refresh_token(self, refresh_token: str) -> SessionData:
        try:
            result = await self.gql.execute(self.refresh_query, {"refresh_token": refresh_token})
            token = result["refreshToken"]["access_token"]
            expires = result["refreshToken"]["expires_in"]
            return SessionData(access_token=token, expires_in=expires)
        except Exception as e:
            raise GraphQLClientError("Token refresh failed", "refresh_token", e) from e
