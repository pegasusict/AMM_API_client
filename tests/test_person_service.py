import pytest
from services import PersonService
from models import Person  # , ListedPerson


@pytest.mark.asyncio
async def test_get_person(gql_client):
    service = PersonService(gql_client)
    person = await service.get(3)
    assert isinstance(person, Person)
    assert person.full_name == "Mock Person"


@pytest.mark.asyncio
async def test_update_person(gql_client):
    service = PersonService(gql_client)
    person = await service.update_person(3, full_name="Updated Person")
    assert person.full_name == "Updated Person"


@pytest.mark.asyncio
async def test_delete_person(gql_client):
    service = PersonService(gql_client)
    result = await service.delete_person(3)
    assert result["success"]


# @pytest.mark.asyncio
# async def test_search_persons(gql_client):
#     service = PersonService(gql_client)
#     results = await service.search("searchPersons", "Query", 5)
#     assert all(isinstance(item, ListedPerson) for item in results)


@pytest.mark.asyncio
async def test_paginate_persons(gql_client):
    service = PersonService(gql_client)
    items, total = await service.paginate_persons(10, 0)
    assert len(items) >= 0
    assert isinstance(total, int)
