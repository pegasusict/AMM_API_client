import pytest
from services.auth_service import AuthService, SessionData


class FakeAuthClient:
    async def execute(self, query, variables=None):
        if "email" in variables:  # type: ignore
            return {"login": {"access_token": "abc123", "expires_in": 3600}}
        else:
            return {"refreshToken": {"access_token": "xyz789", "expires_in": 1800}}


@pytest.mark.asyncio
async def test_login_with_password():
    auth = AuthService(FakeAuthClient())  # type: ignore
    session = await auth.login_with_password("test@example.com", "password")
    assert isinstance(session, SessionData)
    assert not session.is_expired()
