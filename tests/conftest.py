import pytest
from unittest.mock import AsyncMock
from client import AMMGraphQLClient


@pytest.fixture
def mock_gql():
    """Fixture for a mocked GraphQL client."""
    client = AsyncMock(spec=AMMGraphQLClient)
    client.execute = AsyncMock()
    client.subscribe = AsyncMock()
    return client
