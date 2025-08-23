import pytest
from services import AlbumService
from models import Album


@pytest.mark.asyncio
async def test_get_album(gql_client):
    service = AlbumService(gql_client)
    album = await service.get(10)
    assert isinstance(album, Album)
    assert album.title == "Mock Album"


@pytest.mark.asyncio
async def test_update_album(gql_client):
    service = AlbumService(gql_client)
    album = await service.update_album(10, title="Updated Album")
    assert album.title == "Updated Album"


@pytest.mark.asyncio
async def test_delete_album(gql_client):
    service = AlbumService(gql_client)
    result = await service.delete_album(10)
    assert result["success"] is True
