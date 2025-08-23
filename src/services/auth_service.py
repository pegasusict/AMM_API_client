# services/auth_service.py
from typing import Optional

from .base_service import BaseService
from models.user import User


class AuthService(BaseService):
    async def login(self, username: str, password: str) -> dict:
        return await self._exec("login", "login.graphql", {"username": username, "password": password})

    async def me(self) -> Optional[User]:
        result = await self._exec("me", "me.graphql", {})
        return User(**result["me"]) if result["me"] else None

    async def refresh(self, refresh_token: str) -> dict:
        return await self._exec("refresh", "refresh.graphql", {"refreshToken": refresh_token})
