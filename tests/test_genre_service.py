import pytest
from services.genre import GenreService


class MockClient:
    async def execute(self, query, variables=None):
        if "genres" in query:
            return {"genres": [{"id": 1, "name": "Mock Genre"}]}
        elif "searchGenres" in query:
            return {"searchGenres": [{"id": 2, "name": "Found"}]}
        elif "updateGenre" in query:
            return {"updateGenre": {"id": 1, "name": "Updated"}}
        elif "deleteGenre" in query:
            return {"deleteGenre": {"success": True, "message": "Deleted"}}
        return {}


@pytest.mark.asyncio
async def test_genre_read_paginated():
    service = GenreService(MockClient())
    result = await service.read.get_paginated(10, 0)
    assert result[0].name == "Mock Genre"


@pytest.mark.asyncio
async def test_genre_search():
    service = GenreService(MockClient())
    result = await service.read.search("query", 10)
    assert result[0].name == "Found"


@pytest.mark.asyncio
async def test_genre_update():
    service = GenreService(MockClient())
    result = await service.mutate.update(genre_id=1, name="Updated")
    assert result.name == "Updated"


@pytest.mark.asyncio
async def test_genre_delete():
    service = GenreService(MockClient())
    result = await service.mutate.delete(genre_id=1)
    assert result["success"]
