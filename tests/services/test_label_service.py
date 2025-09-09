import pytest
from services import LabelService
from models import Label, ListedLabel


@pytest.mark.asyncio
async def test_get_label(mock_gql):
    mock_gql.execute.return_value = {
        "getLabel": {
            "id": 1,
            "name": "EMI",
            "description": "Record label",
            "albums": [1, 2],
        }
    }

    service = LabelService(mock_gql)
    result = await service.get_label(1)

    assert isinstance(result, Label)
    assert result.id == 1
    assert result.name == "EMI"


@pytest.mark.asyncio
async def test_update_label(mock_gql):
    mock_gql.execute.return_value = {
        "updateLabel": {
            "id": 1,
            "name": "Warner Music",
            "description": "Major label",
            "albums": [3],
        }
    }

    service = LabelService(mock_gql)
    result = await service.update("update_label.graphql", "label", 1, name="Warner Music")

    assert isinstance(result, Label)
    assert result.name == "Warner Music"


@pytest.mark.asyncio
async def test_delete_label(mock_gql):
    mock_gql.execute.return_value = {"deleteLabel": {"success": True}}

    service = LabelService(mock_gql)
    result = await service.delete("delete_label.graphql", "label", 1)

    assert result["success"] is True


@pytest.mark.asyncio
async def test_search_labels(mock_gql):
    mock_gql.execute.return_value = {
        "searchLabels": [
            {"id": 1, "name": "Sony"},
            {"id": 2, "name": "Universal"},
        ]
    }

    service = LabelService(mock_gql)
    results = await service.search("search_labels.graphql", "searchLabels", "sony", 5)

    assert len(results) == 2
    assert isinstance(results[0], ListedLabel)
    assert results[0].name == "Sony"


@pytest.mark.asyncio
async def test_paginate_labels(mock_gql):
    mock_gql.execute.return_value = {"paginatedLabels": {"items": [{"id": 1, "name": "Atlantic"}, {"id": 2, "name": "Virgin"}], "total": 2}}

    service = LabelService(mock_gql)
    items, total = await service.paginate_with_total("paginated_labels.graphql", "paginatedLabels", 10, 0)

    assert len(items) == 2
    assert total == 2
    assert isinstance(items[0], ListedLabel)
