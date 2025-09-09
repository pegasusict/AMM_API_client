import aiohttp
import asyncio
import json
import random
from typing import Any, AsyncGenerator, Optional
from errors import GraphQLClientError


class AMMGraphQLClient:
    """
    Async GraphQL client supporting queries, mutations, and subscriptions.
    """

    def __init__(
        self,
        http_url: str,
        ws_url: Optional[str] = None,
        headers: Optional[dict[str, str]] = None,
        max_retries: int = 5,
        base_backoff: float = 1.0,
        max_backoff: float = 30.0,
    ):
        self.http_url = http_url
        self.ws_url = ws_url or http_url.replace("http", "ws")
        self.headers = headers or {}
        self.max_retries = max_retries
        self.base_backoff = base_backoff
        self.max_backoff = max_backoff
        self._session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession(headers=self.headers)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            await self._session.close()

    async def execute(self, query: str, variables: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        """
        Execute a GraphQL query or mutation over HTTP.
        """
        if not self._session:
            self._session = aiohttp.ClientSession(headers=self.headers)

        try:
            async with self._session.post(
                self.http_url,
                json={"query": query, "variables": variables or {}},
            ) as resp:
                data = await resp.json()
                if "errors" in data:
                    raise GraphQLClientError("GraphQL query failed", query, data["errors"])
                return data["data"]
        except Exception as e:
            raise GraphQLClientError("HTTP execute failed", query, e) from e

    async def subscribe(
        self,
        query: str,
        variables: Optional[dict[str, Any]] = None,
        retry_forever: bool = True,
    ) -> AsyncGenerator[dict[str, Any], None]:
        """
        Execute a GraphQL subscription using WebSockets.
        Will retry with exponential backoff if connection drops.
        """
        import websockets  # lightweight dependency for GraphQL subscriptions

        attempt = 0
        while retry_forever or attempt < self.max_retries:
            try:
                async with websockets.connect(self.ws_url, extra_headers=self.headers) as websocket:
                    # GraphQL WS protocol init
                    await websocket.send(json.dumps({"type": "connection_init", "payload": {}}))
                    await websocket.send(json.dumps({"id": "1", "type": "start", "payload": {"query": query, "variables": variables or {}}}))

                    async for message in websocket:
                        data = json.loads(message)
                        if data.get("type") == "data":
                            yield data["payload"]["data"]
                        elif data.get("type") in ("error", "connection_error"):
                            raise GraphQLClientError("Subscription error", query, data)
                        elif data.get("type") == "complete":
                            return

            except asyncio.CancelledError:
                # Graceful stop
                raise
            except Exception as e:
                attempt += 1
                delay = min(
                    self.base_backoff * (2**attempt) + random.uniform(0, 1),
                    self.max_backoff,
                )
                print(f"[Subscription] Error: {e}, retrying in {delay:.1f}s (attempt {attempt})")
                await asyncio.sleep(delay)

        raise GraphQLClientError("Max retries reached for subscription", query)
