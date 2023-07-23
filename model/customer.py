from pydantic import BaseModel

from model.address import Address


class Customer(BaseModel):
    customer_id: int
    customer_name: str
    first_name: str
    last_name: str
    email_id: str
    phone_number: str
    password: str
    address: Address

