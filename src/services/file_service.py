from models import File, ListedFile
from services import CRUDService
from client import AMMGraphQLClient
from gql import GET_FILE, UPDATE_FILE, DELETE_FILE, PAGINATED_FILES


class FileService(CRUDService):
    """Service for managing files with separate detail and list models."""

    def __init__(self, gql: AMMGraphQLClient):
        super().__init__(gql, list_model=ListedFile, detail_model=File)

    # --- Queries ---

    async def get_file(self, file_id: int) -> File:
        """Fetch a single file by ID with full details."""
        result = await self._exec("get_file", GET_FILE, {"fileId": file_id})
        return File(**result["getFile"])

    async def paginate_files(self, limit: int, offset: int) -> tuple[list[ListedFile], int]:
        """Fetch paginated files with total count (lightweight listing model)."""
        return await self.paginate_with_total(PAGINATED_FILES, "paginatedFiles", limit, offset)

    # --- Mutations ---

    async def update_file(self, file_id: int, **fields) -> File:
        """Update a file’s metadata and return the updated detailed model."""
        return await self.update(UPDATE_FILE, "file", file_id, **fields)

    async def delete_file(self, file_id: int) -> dict:
        """Delete a file by ID."""
        return await self.delete(DELETE_FILE, "file", file_id)
