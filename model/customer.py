from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

from model.address import Address


class Customer(BaseModel):
    customer_id: UUID = uuid4()
    customer_name: str
    first_name: str
    last_name: str
    email_id: str
    phone_number: str
    password: str
    address: Optional[Address] = None

