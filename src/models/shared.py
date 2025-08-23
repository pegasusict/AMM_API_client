from pydantic import BaseModel
from typing import Optional, List, Generic, TypeVar
from datetime import date, datetime

T = TypeVar('T')

class Paginated(BaseModel, Generic[T]):
    items: List[T]
    total: int