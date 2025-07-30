from client import AMMGraphQLClient
from models.display_task import DisplayTask
from models.stat import Stat
from utils.graphql_helpers import load_query
from errors import GraphQLClientError


class TaskService:
    def __init__(self, gql: AMMGraphQLClient):
        self.gql = gql
        self.query_display = load_query("display_tasks")
        self.query_stats = load_query("stats")

    async def get_display_tasks(self) -> list[DisplayTask]:
        try:
            result = await self.gql.execute(self.query_display)
            return [DisplayTask(**task) for task in result["displayTasks"]]
        except Exception as e:
            raise GraphQLClientError("Failed to fetch display tasks", "get_display_tasks", e) from e

    async def get_stats(self) -> list[Stat]:
        try:
            result = await self.gql.execute(self.query_stats)
            return [Stat(**stat) for stat in result["stats"]]
        except Exception as e:
            raise GraphQLClientError("Failed to fetch stats", "get_stats", e) from e
