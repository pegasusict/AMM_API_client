import pytest
from services import GenreService
from models import Genre, ListedGenre


@pytest.mark.asyncio
async def test_get_genre(mock_gql):
    mock_gql.execute.return_value = {
        "getGenre": {
            "id": 1,
            "name": "Rock",
            "description": "Rock music",
            "albums": [1, 2],
            "tracks": [10, 11],
        }
    }

    service = GenreService(mock_gql)
    result = await service.get_genre(1)

    assert isinstance(result, Genre)
    assert result.id == 1
    assert result.name == "Rock"


@pytest.mark.asyncio
async def test_update_genre(mock_gql):
    mock_gql.execute.return_value = {
        "updateGenre": {
            "id": 1,
            "name": "Alternative Rock",
            "description": "Alt Rock",
            "albums": [3],
            "tracks": [12],
        }
    }

    service = GenreService(mock_gql)
    result = await service.update("update_genre.graphql", "genre", 1, name="Alternative Rock")

    assert isinstance(result, Genre)
    assert result.name == "Alternative Rock"


@pytest.mark.asyncio
async def test_delete_genre(mock_gql):
    mock_gql.execute.return_value = {"deleteGenre": {"success": True}}

    service = GenreService(mock_gql)
    result = await service.delete("delete_genre.graphql", "genre", 1)

    assert result["success"] is True


@pytest.mark.asyncio
async def test_search_genres(mock_gql):
    mock_gql.execute.return_value = {
        "searchGenres": [
            {"id": 1, "name": "Jazz"},
            {"id": 2, "name": "Blues"},
        ]
    }

    service = GenreService(mock_gql)
    results = await service.search("search_genres.graphql", "searchGenres", "jazz", 5)

    assert len(results) == 2
    assert isinstance(results[0], ListedGenre)
    assert results[0].name == "Jazz"


@pytest.mark.asyncio
async def test_paginate_genres(mock_gql):
    mock_gql.execute.return_value = {"paginatedGenres": {"items": [{"id": 1, "name": "Hip-Hop"}, {"id": 2, "name": "Classical"}], "total": 2}}

    service = GenreService(mock_gql)
    items, total = await service.paginate_with_total("paginated_genres.graphql", "paginatedGenres", 10, 0)

    assert len(items) == 2
    assert total == 2
    assert isinstance(items[0], ListedGenre)
