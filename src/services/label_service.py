from services.base_crud import CRUDService
from models.label import Label


class LabelService(CRUDService):
    def __init__(self, gql):
        super().__init__(gql, Label)

    async def get_paginated(self, limit: int = 10, offset: int = 0):
        return await super().paginate("paginated_labels", "labels", limit, offset)

    async def search(self, query: str, limit: int = 10):  # type: ignore
        return await super().search("search_labels", "searchLabels", query, limit)

    async def update(self, label_id: int, **fields):  # type: ignore
        return await super().update("update_label", "label", label_id, **fields)

    async def delete(self, label_id: int):  # type: ignore
        return await super().delete("delete_label", "label", label_id)
