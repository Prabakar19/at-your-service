from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

from model.address import Address


class ServiceProvider(BaseModel):
    service_provider_id: UUID = uuid4()
    company_name: str
    owner_name: str
    email_id: str
    contact_number: str
    password: str
    sp_rating: float
    address: Optional[Address] = None
