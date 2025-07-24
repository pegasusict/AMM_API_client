import pytest
from services.user_service import UserService
from models.user import User, PlaybackState


class FakeUserClient:
    async def execute(self, query, variables=None):
        if "playbackState" in query:
            return {"playbackState": {"currentTrackId": "1", "position": 42, "isPlaying": True}}
        return {"me": {"id": "u1", "email": "test@site.com", "name": "Tester"}}


@pytest.mark.asyncio
async def test_get_me():
    service = UserService(FakeUserClient())  # type: ignore
    user = await service.get_me()
    assert isinstance(user, User)


@pytest.mark.asyncio
async def test_playback_state():
    service = UserService(FakeUserClient())  # type: ignore
    state = await service.get_playback_state()
    assert isinstance(state, PlaybackState)
