import pytest
from services.album import AlbumService


class MockClient:
    async def execute(self, query, variables=None):
        if "albums" in query:
            return {"albums": [{"id": 1, "title": "Mock Album"}]}
        elif "searchAlbums" in query:
            return {"searchAlbums": [{"id": 2, "title": "Found"}]}
        elif "updateAlbum" in query:
            return {"updateAlbum": {"id": 1, "title": "Updated"}}
        elif "deleteAlbum" in query:
            return {"deleteAlbum": {"success": True, "message": "Deleted"}}
        return {}


@pytest.mark.asyncio
async def test_album_read_paginated():
    service = AlbumService(MockClient())
    result = await service.read.get_paginated(10, 0)
    assert result[0].title == "Mock Album"


@pytest.mark.asyncio
async def test_album_search():
    service = AlbumService(MockClient())
    result = await service.read.search("query", 10)
    assert result[0].title == "Found"


@pytest.mark.asyncio
async def test_album_update():
    service = AlbumService(MockClient())
    result = await service.mutate.update(album_id=1, title="Updated")
    assert result.title == "Updated"


@pytest.mark.asyncio
async def test_album_delete():
    service = AlbumService(MockClient())
    result = await service.mutate.delete(album_id=1)
    assert result["success"]
