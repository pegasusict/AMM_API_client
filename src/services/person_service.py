from services.crud_service import CRUDService
from models.person import Person
from models.listed.listed_person import ListedPerson


class PersonService(CRUDService):
    def __init__(self, gql):
        super().__init__(gql, list_model=ListedPerson, detail_model=Person)

    async def get(self, person_id: int) -> Person:
        result = await self._exec("get", "get_person.graphql", {"personId": person_id})
        return self.detail_model(**result["person"])  # type: ignore

    async def update_person(self, person_id: int, **fields) -> Person:
        return await self.update("update_person.graphql", "person", person_id, **fields)

    async def delete_person(self, person_id: int):
        return await self.delete("delete_person.graphql", "person", person_id)

    async def paginate_persons(self, limit: int, offset: int):
        return await self.paginate_with_total("paginated_persons.graphql", "paginatedPersons", limit, offset)
