import pytest
from unittest.mock import AsyncMock

from services import PlayerService
from models import PlaybackState, PlayerQueue


@pytest.fixture
def mock_gql():
    return AsyncMock()


@pytest.fixture
def service(mock_gql):
    return PlayerService(mock_gql)


@pytest.mark.asyncio
async def test_get_status(service, mock_gql):
    mock_gql.execute.return_value = {
        "playerStatus": {
            "current_track": {
                "id": 1,
                "title": "Track 1",
                "artists": ["Artist A"],
                "album_picture": None,
                "duration_seconds": 180,
            },
            "is_playing": True,
        }
    }

    result = await service.get_status()
    assert isinstance(result, PlaybackState)
    assert result.is_playing
    assert result.current_track.title == "Track 1"  # type: ignore
    mock_gql.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_queue(service, mock_gql):
    mock_gql.execute.return_value = {
        "playerQueue": {
            "tracks": [
                {
                    "id": 1,
                    "title": "Track 1",
                    "artists": ["Artist A"],
                    "album_picture": None,
                    "duration_seconds": 180,
                },
                {
                    "id": 2,
                    "title": "Track 2",
                    "artists": ["Artist B"],
                    "album_picture": None,
                    "duration_seconds": 200,
                },
            ]
        }
    }

    result = await service.get_queue()
    assert isinstance(result, PlayerQueue)
    assert len(result.tracks) == 2
    assert result.tracks[0].title == "Track 1"
    mock_gql.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_queue_track(service, mock_gql):
    mock_gql.execute.return_value = {"queueTrack": True}
    result = await service.queue_track(123)
    assert result is True
    mock_gql.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_play_next(service, mock_gql):
    mock_gql.execute.return_value = {"playNext": True}
    result = await service.play_next()
    assert result is True
    mock_gql.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_pause(service, mock_gql):
    mock_gql.execute.return_value = {"pause": True}
    result = await service.pause()
    assert result is True
    mock_gql.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_stop(service, mock_gql):
    mock_gql.execute.return_value = {"stop": True}
    result = await service.stop()
    assert result is True
    mock_gql.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_set_position(service, mock_gql):
    mock_gql.execute.return_value = {"setPosition": True}
    result = await service.set_position(90)
    assert result is True
    mock_gql.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_subscribe_status(service, mock_gql):
    async def fake_subscribe(query, variables=None):
        yield {
            "playerStatus": {
                "current_track": {
                    "id": 1,
                    "title": "Track 1",
                    "artists": ["Artist A"],
                    "album_picture": None,
                    "duration_seconds": 180,
                },
                "is_playing": True,
            }
        }

    mock_gql.subscribe = fake_subscribe

    events = []
    async for state in service.subscribe_status():
        assert isinstance(state, PlaybackState)
        events.append(state)
        break  # test only first event

    assert events[0].is_playing
    assert events[0].current_track.title == "Track 1"
