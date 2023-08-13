from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class Address(BaseModel):
    address_id: UUID = uuid4()
    house_address: str
    area: str
    city: str
    state: str
    country: str
    pincode: int
    customer_id: Optional[UUID] = None
    service_provider_id: Optional[UUID] = None
