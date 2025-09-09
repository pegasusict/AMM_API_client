import pytest
from services import FileService
from models import File, ListedFile


@pytest.mark.asyncio
async def test_get_file(mock_gql):
    mock_gql.execute.return_value = {
        "getFile": {
            "id": 1,
            "path": "/music/test.mp3",
            "fileName": "test.mp3",
            "file_type": "audio/mpeg",
            "size": 123456,
            "codec": "mp3",
            "bitrate": 320,
            "duration": 180,
            "stage": "parsed",
            "created_at": "2025-01-01T00:00:00Z",
            "updated_at": "2025-01-01T01:00:00Z",
        }
    }

    service = FileService(mock_gql)
    result = await service.get_file(1)

    assert isinstance(result, File)
    assert result.id == 1
    assert result.fileName == "test.mp3"


@pytest.mark.asyncio
async def test_update_file(mock_gql):
    mock_gql.execute.return_value = {
        "updateFile": {
            "id": 1,
            "path": "/music/updated.mp3",
            "file_name": "updated.mp3",
            "file_type": "audio/mpeg",
            "size": 654321,
            "codec": "aac",
            "bitrate": 256,
            "duration": 200,
            "stage": "trimmed",
            "created_at": "2025-01-01T00:00:00Z",
            "updated_at": "2025-01-01T02:00:00Z",
        }
    }

    service = FileService(mock_gql)
    result = await service.update("update_file.graphql", "file", 1, file_name="updated.mp3")

    assert isinstance(result, File)
    assert result.fileName == "updated.mp3"
    assert result.codec == "aac"


@pytest.mark.asyncio
async def test_delete_file(mock_gql):
    mock_gql.execute.return_value = {"deleteFile": {"success": True}}

    service = FileService(mock_gql)
    result = await service.delete("delete_file.graphql", "file", 1)

    assert result["success"] is True


@pytest.mark.asyncio
async def test_paginate_files(mock_gql):
    mock_gql.execute.return_value = {
        "paginatedFiles": {
            "items": [
                {
                    "id": 1,
                    "path": "/music/1.mp3",
                    "file_name": "1.mp3",
                    "file_type": "audio/mpeg",
                    "size": 1000,
                    "codec": "mp3",
                    "bitrate": 128,
                    "duration": 180,
                    "stage": "parsed",
                    "created_at": "2025-01-01T00:00:00Z",
                    "updated_at": "2025-01-01T01:00:00Z",
                },
                {
                    "id": 2,
                    "path": "/music/2.mp3",
                    "file_name": "2.mp3",
                    "file_type": "audio/mpeg",
                    "size": 2000,
                    "codec": "mp3",
                    "bitrate": 192,
                    "duration": 200,
                    "stage": "parsed",
                    "created_at": "2025-01-01T00:00:00Z",
                    "updated_at": "2025-01-01T01:00:00Z",
                },
            ],
            "total": 2,
        }
    }

    service = FileService(mock_gql)
    items, total = await service.paginate_with_total("paginated_files.graphql", "paginatedFiles", 10, 0)

    assert len(items) == 2
    assert total == 2
    assert isinstance(items[0], ListedFile)
