from client import AMMGraphQLClient
from services.track_service import TrackService
from services.auth_service import AuthService
from services.user_service import UserService
from services.stream_service import StreamService
from session import PersistentSession


class AMMClient:
    def __init__(self, base_url: str, persist: bool = True):
        self.endpoint = f"{base_url}/graphql"
        self.stream_url = base_url
        self.session = PersistentSession(enabled=persist)
        self.token = self.session.load_token()

        self.gql = AMMGraphQLClient(token=self.token or "", endpoint=self.endpoint)
        self.track = TrackService(self.gql)
        self.auth = AuthService(self.gql)
        self.user = UserService(self.gql)
        self.stream = StreamService(self.stream_url)

    async def login(self, email: str, password: str) -> None:
        session_data = await self.auth.login_with_password(email, password)
        self.token = session_data.access_token
        self.session.save_token(self.token)
        self.gql = AMMGraphQLClient(token=self.token, endpoint=self.endpoint)
        self._refresh_services()

    async def refresh(self, refresh_token: str) -> None:
        session_data = await self.auth.refresh_token(refresh_token)
        self.token = session_data.access_token
        self.session.save_token(self.token)
        self.gql = AMMGraphQLClient(token=self.token, endpoint=self.endpoint)
        self._refresh_services()

    def _refresh_services(self):
        self.track = TrackService(self.gql)
        self.user = UserService(self.gql)
