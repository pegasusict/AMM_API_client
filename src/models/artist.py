from pydantic import BaseModel
from typing import Optional
from datetime import date


class Person(BaseModel):
    id: Optional[int]
    full_name: Optional[str]
    alias: Optional[str]
    nick_name: Optional[str]
    date_of_birth: Optional[date]
