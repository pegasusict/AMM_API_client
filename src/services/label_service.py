from client import AMMGraphQLClient
from utils.graphql_helpers import load_query
from models.label import Label


class LabelService:
    def __init__(self, gql: AMMGraphQLClient):
        self.gql = gql

    async def update(self, label_id: int, **kwargs) -> Label:
        query = load_query("update_label")
        result = await self.gql.execute(query, {"labelId": label_id, "input": kwargs})
        return Label(**result["updateLabel"])

    async def delete(self, label_id: int) -> dict:
        query = load_query("delete_label")
        result = await self.gql.execute(query, {"labelId": label_id})
        return result["deleteLabel"]
