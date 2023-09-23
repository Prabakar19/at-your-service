from typing import Any, List
from uuid import UUID
from pydantic import BaseModel
from model.transaction import Transaction
from utils.id_generator import IdGenerator


class Service(BaseModel):
    service_id: UUID = IdGenerator.generate_uuid()
    service_name: str
    cost: float
    discount: float
    discounted_cost: float
    discount_availability: bool
    details: str
    warranty: float
    service_provider_id: UUID
    category_id: UUID
    rating: float
    city: str
    short_description: str
    service_pic: Any = ''  # TODO: find datatype for all the picture variable
    # transactions: List[Transaction]  # TODO: change any


class ServiceRequest(BaseModel):
    serviceName: str
    cost: float
    discount: float
    discountAvailability: bool
    details: str
    warranty: float
    serviceProviderId: UUID
    categoryId: UUID