from services.crud_service import CRUDService
from models.label import Label
from models.listed.listed_label import ListedLabel


class LabelService(CRUDService):
    def __init__(self, gql):
        super().__init__(gql, list_model=ListedLabel, detail_model=Label)

    async def get(self, label_id: int) -> Label:
        result = await self._exec("get", "get_label.graphql", {"labelId": label_id})
        return self.detail_model(**result["label"])  # type: ignore

    async def update_label(self, label_id: int, **fields) -> Label:
        return await self.update("update_label.graphql", "label", label_id, **fields)

    async def delete_label(self, label_id: int):
        return await self.delete("delete_label.graphql", "label", label_id)

    async def paginate_labels(self, limit: int, offset: int):
        return await self.paginate_with_total("paginated_labels.graphql", "paginatedLabels", limit, offset)
