import pytest
import httpx
from client import AMMGraphQLClient


class MockGraphQLServer:
    """A simple in-memory GraphQL server for tests."""

    def __init__(self):
        self.handlers = {}

    def add_handler(self, operation_name: str, response: dict):
        """Register a fake GraphQL response for an operation."""
        self.handlers[operation_name] = response

    def handler(self, request: httpx.Request) -> httpx.Response:
        """httpx transport handler."""
        payload = request.json()  # type: ignore
        operation_name = payload.get("operationName")

        if operation_name in self.handlers:
            return httpx.Response(200, json={"data": self.handlers[operation_name]})
        return httpx.Response(400, json={"errors": [{"message": f"Unknown operation {operation_name}"}]})


@pytest.fixture
def mock_server():
    """Fixture providing a pre-populated mock GraphQL server."""
    server = MockGraphQLServer()

    # --- User ---
    server.add_handler(
        "Me",
        {
            "me": {
                "id": 1,
                "username": "testuser",
                "email": "test@example.com",
                "role": "ADMIN",
                "is_active": True,
            }
        },
    )
    server.add_handler("Login", {"login": {"accessToken": "fake-token"}})
    server.add_handler("Refresh", {"refresh": {"accessToken": "new-token"}})

    # --- Tracks ---
    server.add_handler("GetTrack", {"getTrack": {"id": 42, "title": "Mock Track", "albumId": 10}})
    server.add_handler("UpdateTrack", {"updateTrack": {"id": 42, "title": "Updated Track"}})
    server.add_handler("DeleteTrack", {"deleteTrack": {"success": True}})
    server.add_handler("SearchTracks", {"searchTracks": [{"id": 1, "title": "Result A"}, {"id": 2, "title": "Result B"}]})
    server.add_handler("PaginatedTracks", {"paginatedTracks": {"items": [{"id": 1, "title": "PageTrack"}], "total": 1}})

    # --- Albums ---
    server.add_handler("GetAlbum", {"getAlbum": {"id": 10, "title": "Mock Album"}})
    server.add_handler("UpdateAlbum", {"updateAlbum": {"id": 10, "title": "Updated Album"}})
    server.add_handler("DeleteAlbum", {"deleteAlbum": {"success": True}})

    # --- Genres ---
    server.add_handler("GetGenre", {"getGenre": {"id": 5, "name": "Mock Genre"}})
    server.add_handler("UpdateGenre", {"updateGenre": {"id": 5, "name": "Updated Genre"}})
    server.add_handler("DeleteGenre", {"deleteGenre": {"success": True}})

    # --- Labels ---
    server.add_handler("GetLabel", {"getLabel": {"id": 7, "name": "Mock Label"}})
    server.add_handler("UpdateLabel", {"updateLabel": {"id": 7, "name": "Updated Label"}})
    server.add_handler("DeleteLabel", {"deleteLabel": {"success": True}})

    # --- Persons ---
    server.add_handler("GetPerson", {"getPerson": {"id": 3, "name": "Mock Artist"}})
    server.add_handler("UpdatePerson", {"updatePerson": {"id": 3, "name": "Updated Artist"}})
    server.add_handler("DeletePerson", {"deletePerson": {"success": True}})

    # --- Files ---
    server.add_handler("GetFile", {"getFile": {"id": 99, "path": "/mock/file.mp3"}})
    server.add_handler("DeleteFile", {"deleteFile": {"success": True}})

    # --- Tasks ---
    server.add_handler(
        "Tasks",
        {
            "tasks": [
                {"id": 1, "type": "IMPORT", "status": "PENDING"},
                {"id": 2, "type": "PARSE", "status": "DONE"},
            ]
        },
    )
    server.add_handler("TaskStats", {"taskStats": {"taskType": "IMPORT", "imported": 100, "parsed": 50}})
    server.add_handler("TaskStatTrend", {"taskStatTrend": {"taskType": "IMPORT", "imported": [], "parsed": []}})
    server.add_handler("TaskStatSummary", {"taskStatSummary": {"taskType": "IMPORT", "imported": {"value": 10, "change": 5, "percentage": 100.0}}})

    return server


@pytest.fixture
def gql_client(mock_server):
    """Fixture that provides AMMGraphQLClient with a mocked transport."""
    transport = httpx.MockTransport(mock_server.handler)
    return AMMGraphQLClient(
        token="testtoken",
        endpoint="http://testserver/graphql",
        transport=transport,  # type: ignore
    )
