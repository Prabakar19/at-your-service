from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Address(BaseModel):
    address_id: UUID
    house_address: str
    area: str
    city: str
    state: str
    country: str
    pincode: int
    customer_id: Optional[UUID] = None
    service_provider_id: Optional[UUID] = None
