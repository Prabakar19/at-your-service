from typing import Any, List
from uuid import UUID
from pydantic import BaseModel

from model.service import Service


class Category(BaseModel):
    category_id: UUID
    category_name: str
    category_pic: Any  # TODO: find datatype for all the picture variable
    services: List[Service]
