import pytest
from services import LabelService
from models import Label, ListedLabel


@pytest.mark.asyncio
async def test_get_label(gql_client):
    service = LabelService(gql_client)
    label = await service.get(7)
    assert isinstance(label, Label)
    assert label.name == "Mock Label"


@pytest.mark.asyncio
async def test_update_label(gql_client):
    service = LabelService(gql_client)
    label = await service.update_label(7, name="Updated Label")
    assert label.name == "Updated Label"


@pytest.mark.asyncio
async def test_delete_label(gql_client):
    service = LabelService(gql_client)
    result = await service.delete_label(7)
    assert result["success"]


@pytest.mark.asyncio
async def test_paginate_labels(gql_client):
    service = LabelService(gql_client)
    items, total = await service.paginate_labels(10, 0)
    assert len(items) >= 0
    assert isinstance(total, int)
