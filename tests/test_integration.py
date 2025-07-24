import pytest
from amm_client import AMMClient


@pytest.mark.asyncio
async def test_client_login_and_tracks(monkeypatch):
    # Fake test credentials for local dev/test
    monkeypatch.setenv("AMM_API_TEST_USER", "test@example.com")
    monkeypatch.setenv("AMM_API_TEST_PASS", "secret")

    email = "test@example.com"
    password = "secret"

    client = AMMClient("http://localhost:8000", persist=False)
    await client.login(email, password)

    me = await client.user.get_me()
    assert me.email == email

    tracks = await client.track.get_tracks(limit=2)
    assert isinstance(tracks, list)
