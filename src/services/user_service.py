from models import User, ListedUser
from .crud_service import CRUDService
from gql import (
    GET_USER,
    UPDATE_USER,
    DELETE_USER,
    SEARCH_USERS,
    PAGINATED_USERS,
    LOGIN,
    ME,
    REFRESH,
)


class UserService(CRUDService):
    """Service for managing users + auth."""

    def __init__(self, gql_client):
        super().__init__(gql_client, list_model=ListedUser, detail_model=User)

    async def get(self, user_id: int) -> User:
        result = await self._exec("get_user", GET_USER, {"userId": user_id})
        return User(**result["getUser"])

    async def update_user(self, user_id: int, **fields) -> User:
        return await self.update(UPDATE_USER, "user", user_id, **fields)

    async def delete_user(self, user_id: int) -> bool:
        return await self.delete(DELETE_USER, "user", user_id)  # type: ignore

    async def search_users(self, query: str, limit: int = 10) -> list[ListedUser]:
        return await self.search(SEARCH_USERS, "searchUsers", query, limit)

    async def paginate_users(self, limit: int = 10, offset: int = 0):
        return await self.paginate_with_total(PAGINATED_USERS, "paginatedUsers", limit, offset)

    # ---- Auth-specific methods ----
    async def login(self, username: str, password: str) -> dict:
        result = await self._exec("login", LOGIN, {"username": username, "password": password})
        return result["login"]

    async def me(self) -> User:
        result = await self._exec("me", ME)
        return User(**result["me"])

    async def refresh(self, refresh_token: str) -> dict:
        result = await self._exec("refresh", REFRESH, {"refreshToken": refresh_token})
        return result["refresh"]
