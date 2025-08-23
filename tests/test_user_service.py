import pytest
from services import UserService
from models import User


@pytest.mark.asyncio
async def test_me(gql_client):
    service = UserService(gql_client)
    user = await service.me()
    assert isinstance(user, User)
    assert user.username == "testuser"


@pytest.mark.asyncio
async def test_login(gql_client):
    service = UserService(gql_client)
    result = await service.login("u", "p")
    assert "accessToken" in result
    assert result["accessToken"] == "fake-token"


@pytest.mark.asyncio
async def test_refresh(gql_client):
    service = UserService(gql_client)
    result = await service.refresh("refresh-token")
    assert result["accessToken"] == "new-token"
