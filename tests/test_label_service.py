import pytest
from services.label import LabelService


class MockClient:
    async def execute(self, query, variables=None):
        if "labels" in query:
            return {"labels": [{"id": 1, "name": "Mock Label"}]}
        elif "searchLabels" in query:
            return {"searchLabels": [{"id": 2, "name": "Found"}]}
        elif "updateLabel" in query:
            return {"updateLabel": {"id": 1, "name": "Updated"}}
        elif "deleteLabel" in query:
            return {"deleteLabel": {"success": True, "message": "Deleted"}}
        return {}


@pytest.mark.asyncio
async def test_label_read_paginated():
    service = LabelService(MockClient())
    result = await service.read.get_paginated(10, 0)
    assert result[0].name == "Mock Label"


@pytest.mark.asyncio
async def test_label_search():
    service = LabelService(MockClient())
    result = await service.read.search("query", 10)
    assert result[0].name == "Found"


@pytest.mark.asyncio
async def test_label_update():
    service = LabelService(MockClient())
    result = await service.mutate.update(label_id=1, name="Updated")
    assert result.name == "Updated"


@pytest.mark.asyncio
async def test_label_delete():
    service = LabelService(MockClient())
    result = await service.mutate.delete(label_id=1)
    assert result["success"]
