# tests/test_auth_service.py
import pytest
from services.auth_service import AuthService


@pytest.fixture
def service(mock_gql):
    return AuthService(mock_gql)


@pytest.mark.asyncio
async def test_login(service, mock_gql):
    mock_gql.execute.return_value = {"login": {"accessToken": "abc", "refreshToken": "xyz"}}
    result = await service.login("user", "pass")
    assert result["accessToken"] == "abc"


@pytest.mark.asyncio
async def test_refresh(service, mock_gql):
    mock_gql.execute.return_value = {"refresh": {"accessToken": "newtoken"}}
    result = await service.refresh("refreshtoken")
    assert result["accessToken"] == "newtoken"


@pytest.mark.asyncio
async def test_me(service, mock_gql):
    mock_gql.execute.return_value = {"me": {"id": 1, "username": "test"}}
    result = await service.me()
    assert result["username"] == "test"
