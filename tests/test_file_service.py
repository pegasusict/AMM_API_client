import pytest
from services import FileService
from models import File, ListedFile


@pytest.mark.asyncio
async def test_get_file(gql_client):
    service = FileService(gql_client)
    file = await service.get(99)
    assert isinstance(file, File)
    assert file.filename.endswith(".mp3")


@pytest.mark.asyncio
async def test_delete_file(gql_client):
    service = FileService(gql_client)
    result = await service.delete_file(99)
    assert result["success"]


@pytest.mark.asyncio
async def test_paginate_files(gql_client):
    service = FileService(gql_client)
    items, total = await service.paginate_files(10, 0)
    assert all(isinstance(item, ListedFile) for item in items)
    assert isinstance(total, int)
