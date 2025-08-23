from client import AMMGraphQLClient
from models import File, ListedFile
from .crud_service import CRUDService
from gql import (
    GET_FILE,
    FILES,
    UPDATE_FILE,
    DELETE_FILE,
    PAGINATED_FILES,
)


class FileService(CRUDService):
    """Service for managing files (update, delete, search, paginate)."""

    def __init__(self, gql: AMMGraphQLClient):
        super().__init__(gql, list_model=ListedFile, detail_model=File)

    async def get(self, file_id: int) -> File:
        result = await self._exec("get", GET_FILE, {"fileId": file_id})
        return self.detail_model(**result["file"])  # type: ignore

    async def get_files(self) -> list[ListedFile]:
        """Fetch a list of files."""
        result = await self._exec("list", FILES, {})
        return [ListedFile(**item) for item in result["files"]]

    async def update_file(self, file_id: int, **fields) -> File:
        """Update a file and return its details."""
        return await self.update(UPDATE_FILE, "file", file_id, **fields)

    async def delete_file(self, file_id: int) -> dict:
        """Delete a file by ID."""
        return await self.delete(DELETE_FILE, "file", file_id)

    async def paginate_files(self, limit: int, offset: int) -> tuple[list[ListedFile], int]:
        """Paginate files with total count."""
        return await self.paginate_with_total(PAGINATED_FILES, "paginatedFiles", limit, offset)
