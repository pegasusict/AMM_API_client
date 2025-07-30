from services.base_crud import CRUDService
from models.person import Person


class PersonService(CRUDService):
    def __init__(self, gql):
        super().__init__(gql, Person)

    async def get_paginated(self, limit: int = 10, offset: int = 0):
        return await super().paginate("paginated_persons", "persons", limit, offset)

    async def search(self, query: str, limit: int = 10):  # type: ignore
        return await super().search("search_persons", "searchPersons", query, limit)

    async def update(self, person_id: int, **fields):  # type: ignore
        return await super().update("update_person", "person", person_id, **fields)

    async def delete(self, person_id: int):  # type: ignore
        return await super().delete("delete_person", "person", person_id)
