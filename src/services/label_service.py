from models import Label, ListedLabel
from .crud_service import CRUDService
from gql import (
    GET_LABEL,
    UPDATE_LABEL,
    DELETE_LABEL,
    PAGINATED_LABELS,
)


class LabelService(CRUDService):
    """Service for managing record labels."""

    def __init__(self, gql_client):
        super().__init__(gql_client, list_model=ListedLabel, detail_model=Label)

    async def get_label(self, label_id: int) -> Label:
        result = await self._exec("get_label", GET_LABEL, {"labelId": label_id})
        return Label(**result["getLabel"])

    async def update_label(self, label_id: int, **fields) -> Label:
        return await self.update(UPDATE_LABEL, "label", label_id, **fields)

    async def delete_label(self, label_id: int) -> bool:
        return await self.delete(DELETE_LABEL, "label", label_id)  # type: ignore

    async def paginate_labels(self, limit: int = 10, offset: int = 0):
        return await self.paginate_with_total(PAGINATED_LABELS, "paginatedLabels", limit, offset)
