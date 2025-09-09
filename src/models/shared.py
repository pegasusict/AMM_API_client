from pydantic import BaseModel
from typing import List, Generic, TypeVar


T = TypeVar("T")


class Paginated(BaseModel, Generic[T]):
    items: List[T]
    total: int
