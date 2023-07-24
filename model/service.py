from typing import Any, List
from uuid import UUID
from pydantic import BaseModel
from model.transaction import Transaction


class Service(BaseModel):
    service_id: UUID
    service_name: str
    cost: float
    discount: float
    discounted_cost: float
    discount_availability: bool
    details: str
    warranty: float
    service_provider_id: UUID
    category_id: UUID
    service_ratings: float
    rating: float
    service_pic: Any  # TODO: find datatype for all the picture variable
    transactions: List[Transaction]  # TODO: change any
