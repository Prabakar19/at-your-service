from typing import List
from uuid import UUID
from pydantic import BaseModel

from model.address import Address
from model.category import Category
from model.service import Service
from model.billing import Billing


class ServiceProvider(BaseModel):
    service_provider_id: UUID
    company_name: str
    owner_name: str
    email_id: str
    contact_number: str
    password: str
    service_provider_address: Address
    sp_rating: float
    categories: List[Category]
    services: List[Service]
    billings: List[Billing]
