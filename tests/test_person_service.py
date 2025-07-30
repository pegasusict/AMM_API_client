import pytest
from services.person import PersonService


class MockClient:
    async def execute(self, query, variables=None):
        if "persons" in query:
            return {"persons": [{"id": 1, "full_name": "Mock Person"}]}
        elif "searchPersons" in query:
            return {"searchPersons": [{"id": 2, "full_name": "Found"}]}
        elif "updatePerson" in query:
            return {"updatePerson": {"id": 1, "full_name": "Updated"}}
        elif "deletePerson" in query:
            return {"deletePerson": {"success": True, "message": "Deleted"}}
        return {}


@pytest.mark.asyncio
async def test_person_read_paginated():
    service = PersonService(MockClient())
    result = await service.read.get_paginated(10, 0)
    assert result[0].full_name == "Mock Person"


@pytest.mark.asyncio
async def test_person_search():
    service = PersonService(MockClient())
    result = await service.read.search("query", 10)
    assert result[0].full_name == "Found"


@pytest.mark.asyncio
async def test_person_update():
    service = PersonService(MockClient())
    result = await service.mutate.update(person_id=1, full_name="Updated")
    assert result.full_name == "Updated"


@pytest.mark.asyncio
async def test_person_delete():
    service = PersonService(MockClient())
    result = await service.mutate.delete(person_id=1)
    assert result["success"]
