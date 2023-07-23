from pydantic import BaseModel


class Address(BaseModel):
    address_id: int
    house_address: str
    area: str
    city: str
    state: str
    country: str
    pincode: int
