from .base import LabelBaseService
from models.label import Label


class LabelMutateService(LabelBaseService):
    async def update(self, label_id: int, **kwargs) -> Label:
        result = await self._exec("update_label", "update_label", {"labelId": label_id, "input": kwargs})
        return Label(**result["updateLabel"])

    async def delete(self, label_id: int) -> dict:
        result = await self._exec("delete_label", "delete_label", {"labelId": label_id})
        return result["deleteLabel"]
