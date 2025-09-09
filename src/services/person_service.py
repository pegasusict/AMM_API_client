from models import Person, ListedPerson
from . import CRUDService
from gql import (
    GET_PERSON,
    UPDATE_PERSON,
    DELETE_PERSON,
    PAGINATED_PERSONS,
)


class PersonService(CRUDService):
    """Service for managing people (artists, composers, etc.)."""

    def __init__(self, gql_client):
        super().__init__(gql_client, list_model=ListedPerson, detail_model=Person)

    async def get_person(self, person_id: int) -> Person:
        result = await self._exec("get_person", GET_PERSON, {"personId": person_id})
        return Person(**result["getPerson"])

    async def update_person(self, person_id: int, **fields) -> Person:
        return await self.update(UPDATE_PERSON, "person", person_id, **fields)

    async def delete_person(self, person_id: int) -> bool:
        return await self.delete(DELETE_PERSON, "person", person_id)  # type: ignore

    async def paginate_persons(self, limit: int = 10, offset: int = 0):
        return await self.paginate_with_total(PAGINATED_PERSONS, "paginatedPersons", limit, offset)
