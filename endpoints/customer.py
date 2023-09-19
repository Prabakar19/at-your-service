from typing import Dict

from fastapi import APIRouter

from model.customer import Customer, CustomerRequest
from service.address_service import AddressService
from service.customer_service import CustomerService

customer_router = APIRouter(
    prefix="/customer",
    tags=["Customer APIs"],
    responses={404: {"description": "Not found"}},
)

# TODO: add password reset api

@customer_router.get("/{customer_id}")
async def get_customer(customer_id: str):
    customer_service = CustomerService()
    return await customer_service.get_customer(customer_id)


@customer_router.post("/")
async def add_customer(customer: Customer):
    customer_service = CustomerService()
    await customer_service.add_customer(customer)
    return {'data': 'Customer added successfully'}


@customer_router.put("")
async def update_customer(customer: CustomerRequest):
    customer_service = CustomerService()
    return await customer_service.update_customer(customer)


@customer_router.post("/login")
async def login_customer(login_details: Dict[str, str]):
    customer_service = CustomerService()
    customer_details = await customer_service.customer_login(login_details)
    return customer_details if customer_details else {'data': 'Customer not found'}


@customer_router.get("/address/{customer_id}")
async def get_customer_address(customer_id: str):
    addr_service = AddressService()
    return await addr_service.get_customer_address(customer_id)
