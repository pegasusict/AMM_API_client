import pytest
from services import PlayerService
from models import PlayerStatus


@pytest.mark.asyncio
async def test_get_player_status(gql_client):
    service = PlayerService(gql_client)
    status = await service.get_player_status()
    assert isinstance(status, PlayerStatus)
    assert status.state in ["PLAYING", "PAUSED", "STOPPED"]


@pytest.mark.asyncio
async def test_get_player_queue(gql_client):
    service = PlayerService(gql_client)
    queue = await service.get_player_queue()
    assert isinstance(queue, list)


@pytest.mark.asyncio
async def test_subscribe_player_status(gql_client):
    service = PlayerService(gql_client)
    async for update in service.subscribe_player_status():
        assert isinstance(update, PlayerStatus)
        break  # stop after first update
