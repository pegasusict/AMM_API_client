from client import AMMGraphQLClient
from utils.graphql_helpers import load_query
from models.person import Person


class PersonService:
    def __init__(self, gql: AMMGraphQLClient):
        self.gql = gql

    async def update(self, person_id: int, **kwargs) -> Person:
        query = load_query("update_person")
        result = await self.gql.execute(query, {"personId": person_id, "input": kwargs})
        return Person(**result["updatePerson"])

    async def delete(self, person_id: int) -> dict:
        query = load_query("delete_person")
        result = await self.gql.execute(query, {"personId": person_id})
        return result["deletePerson"]
