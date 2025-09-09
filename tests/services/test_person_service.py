import pytest
from services import PersonService
from models import Person, ListedPerson


@pytest.mark.asyncio
async def test_get_person(mock_gql):
    mock_gql.execute.return_value = {
        "getPerson": {
            "id": 1,
            "full_name": "Freddie Mercury",
            "alias": "Farrokh Bulsara",
            "performed_tracks": [1, 2],
        }
    }

    service = PersonService(mock_gql)
    result = await service.get_person(1)

    assert isinstance(result, Person)
    assert result.id == 1
    assert result.full_name == "Freddie Mercury"


@pytest.mark.asyncio
async def test_update_person(mock_gql):
    mock_gql.execute.return_value = {
        "updatePerson": {
            "id": 1,
            "full_name": "Brian May",
            "alias": "Dr. May",
            "performed_tracks": [3],
        }
    }

    service = PersonService(mock_gql)
    result = await service.update("update_person.graphql", "person", 1, full_name="Brian May")

    assert isinstance(result, Person)
    assert result.full_name == "Brian May"


@pytest.mark.asyncio
async def test_delete_person(mock_gql):
    mock_gql.execute.return_value = {"deletePerson": {"success": True}}

    service = PersonService(mock_gql)
    result = await service.delete("delete_person.graphql", "person", 1)

    assert result["success"] is True


@pytest.mark.asyncio
async def test_search_persons(mock_gql):
    mock_gql.execute.return_value = {
        "searchPersons": [
            {"id": 1, "full_name": "John Lennon"},
            {"id": 2, "full_name": "Paul McCartney"},
        ]
    }

    service = PersonService(mock_gql)
    results = await service.search("search_persons.graphql", "searchPersons", "john", 5)

    assert len(results) == 2
    assert isinstance(results[0], ListedPerson)
    assert results[0].full_name == "John Lennon"


@pytest.mark.asyncio
async def test_paginate_persons(mock_gql):
    mock_gql.execute.return_value = {
        "paginatedPersons": {"items": [{"id": 1, "full_name": "George Harrison"}, {"id": 2, "full_name": "Ringo Starr"}], "total": 2}
    }

    service = PersonService(mock_gql)
    items, total = await service.paginate_with_total("paginated_persons.graphql", "paginatedPersons", 10, 0)

    assert len(items) == 2
    assert total == 2
    assert isinstance(items[0], ListedPerson)
