import pytest
from services.album_service import AlbumService
from models.album import Album


class FakeAlbumClient:
    async def execute(self, query, variables=None):
        if "paginated_albums" in query or "albums(limit:" in query:
            return {"albums": [{"id": 1, "title": "Test Album", "releasedate": "2020-01-01", "genres": [1], "label": "Label A", "track_count": 10}]}

        elif "searchAlbums" in query:
            return {"searchAlbums": [{"id": 2, "title": "Search Match", "releasedate": "1999-01-01"}]}

        elif "updateAlbum" in query:
            return {
                "updateAlbum": {
                    "id": variables["albumId"],  # type: ignore
                    "title": variables["input"].get("title", "Untitled"),  # type: ignore
                    "subtitle": None,
                    "label": "Label X",
                    "releasedate": "2000-01-01",
                }
            }

        elif "deleteAlbum" in query:
            return {"deleteAlbum": {"success": True, "message": "Album deleted"}}

        return {}


@pytest.mark.asyncio
async def test_get_paginated_albums():
    service = AlbumService(FakeAlbumClient())  # type: ignore
    albums = await service.get_paginated(limit=1, offset=0)
    assert isinstance(albums, list)
    assert isinstance(albums[0], Album)
    assert albums[0].title == "Test Album"


@pytest.mark.asyncio
async def test_search_albums():
    service = AlbumService(FakeAlbumClient())  # type: ignore
    results = await service.search("search")
    assert isinstance(results[0], Album)
    assert results[0].title == "Search Match"


@pytest.mark.asyncio
async def test_update_album():
    service = AlbumService(FakeAlbumClient())  # type: ignore
    updated = await service.update(album_id=1, title="Updated Title")
    assert isinstance(updated, Album)
    assert updated.title == "Updated Title"
    assert updated.label == "Label X"


@pytest.mark.asyncio
async def test_delete_album():
    service = AlbumService(FakeAlbumClient())  # type: ignore
    result = await service.delete(album_id=1)
    assert result["success"] is True
    assert result["message"] == "Album deleted"
