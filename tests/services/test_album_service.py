import pytest
from services import AlbumService
from models import Album, ListedAlbum


@pytest.mark.asyncio
async def test_get_album(mock_gql):
    mock_gql.execute.return_value = {
        "getAlbum": {
            "id": 1,
            "title": "Test Album",
            "release_year": 2023,
            "genre": "Rock",
            "artist": "Test Artist",
            "label": "Test Label",
        }
    }

    service = AlbumService(mock_gql)
    result = await service.get_album(1)

    assert isinstance(result, Album)
    assert result.id == 1
    assert result.title == "Test Album"


@pytest.mark.asyncio
async def test_update_album(mock_gql):
    mock_gql.execute.return_value = {
        "updateAlbum": {
            "id": 1,
            "title": "Updated Album",
            "release_year": 2023,
            "genre": "Pop",
            "artist": "New Artist",
            "label": "Test Label",
        }
    }

    service = AlbumService(mock_gql)
    result = await service.update("update_album.graphql", "album", 1, title="Updated Album")

    assert isinstance(result, Album)
    assert result.title == "Updated Album"


@pytest.mark.asyncio
async def test_delete_album(mock_gql):
    mock_gql.execute.return_value = {"deleteAlbum": {"success": True}}

    service = AlbumService(mock_gql)
    result = await service.delete("delete_album.graphql", "album", 1)

    assert result["success"] is True


@pytest.mark.asyncio
async def test_paginate_albums(mock_gql):
    mock_gql.execute.return_value = {
        "paginatedAlbums": {
            "items": [
                {"id": 1, "title": "Album 1", "release_year": 2020, "genre": "Rock", "artist": "A", "label": "X"},
                {"id": 2, "title": "Album 2", "release_year": 2021, "genre": "Jazz", "artist": "B", "label": "Y"},
            ],
            "total": 2,
        }
    }

    service = AlbumService(mock_gql)
    items, total = await service.paginate_with_total("paginated_albums.graphql", "paginatedAlbums", 10, 0)

    assert len(items) == 2
    assert total == 2
    assert isinstance(items[0], ListedAlbum)
