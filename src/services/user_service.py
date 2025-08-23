from typing import Optional
from client import AMMGraphQLClient
from models.user import User
from .crud_service import CRUDService


class UserService(CRUDService):
    """Service for user management (CRUD + authentication)."""

    def __init__(self, gql: AMMGraphQLClient):
        super().__init__(gql, list_model=User, detail_model=User)

    # --- CRUD methods ---
    async def update_user(self, user_id: int, **fields) -> User:
        return await self.update("update_user.graphql", "user", user_id, **fields)

    async def delete_user(self, user_id: int) -> dict:
        return await self.delete("delete_user.graphql", "user", user_id)

    async def search_users(self, query: str, limit: int = 20) -> list[User]:
        return await self.search("search_users.graphql", "searchUsers", query, limit)

    async def paginate_users(self, limit: int, offset: int) -> tuple[list[User], int]:
        return await self.paginate_with_total("paginated_users.graphql", "paginatedUsers", limit, offset)

    # --- Authentication / Profile ---
    async def login(self, username: str, password: str) -> dict:
        return await self._exec("login", "login.graphql", {"username": username, "password": password})

    async def me(self) -> Optional[User]:
        result = await self._exec("me", "me.graphql", {})
        return User(**result["me"]) if result["me"] else None

    async def refresh(self, refresh_token: str) -> dict:
        return await self._exec("refresh", "refresh.graphql", {"refreshToken": refresh_token})
