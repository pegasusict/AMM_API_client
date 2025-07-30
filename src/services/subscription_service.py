from gql import Client, gql
from gql.transport.websockets import WebsocketsTransport
from utils.graphql_helpers import load_query


class SubscriptionService:
    def __init__(self, token: str, ws_url: str):
        self.transport = WebsocketsTransport(url=ws_url, headers={"Authorization": f"Bearer {token}"})
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    async def subscribe_to_player_status(self, on_update):
        query = gql(load_query("player_status_subscription"))
        async with self.client as session:
            async for result in session.subscribe(query):
                on_update(result["playerStatus"])
