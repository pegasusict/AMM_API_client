from .base import PersonBaseService
from models.person import Person


class PersonMutateService(PersonBaseService):
    async def update(self, person_id: int, **kwargs) -> Person:
        result = await self._exec("update_person", "update_person", {"personId": person_id, "input": kwargs})
        return Person(**result["updatePerson"])

    async def delete(self, person_id: int) -> dict:
        result = await self._exec("delete_person", "delete_person", {"personId": person_id})
        return result["deletePerson"]
