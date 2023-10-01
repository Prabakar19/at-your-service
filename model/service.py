from typing import Any, Optional
from uuid import UUID

from pydantic import BaseModel

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


class ServiceRequest(BaseModel):
    serviceName: str
    cost: float
    discount: Optional[float] = 0
    discountAvailability: bool
    details: str
    warranty: float
    serviceProviderId: UUID
    categoryId: UUID
    city: str
