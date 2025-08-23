import pytest
from services import GenreService
from models import Genre, ListedGenre


@pytest.mark.asyncio
async def test_get_genre(gql_client):
    service = GenreService(gql_client)
    genre = await service.get(5)
    assert isinstance(genre, Genre)
    assert genre.name == "Mock Genre"


@pytest.mark.asyncio
async def test_update_genre(gql_client):
    service = GenreService(gql_client)
    genre = await service.update_genre(5, name="Updated Genre")
    assert genre.name == "Updated Genre"


@pytest.mark.asyncio
async def test_delete_genre(gql_client):
    service = GenreService(gql_client)
    result = await service.delete_genre(5)
    assert result["success"]


@pytest.mark.asyncio
async def test_paginate_genres(gql_client):
    service = GenreService(gql_client)
    items, total = await service.paginate_genres(10, 0)
    assert len(items) >= 0
    assert isinstance(total, int)
