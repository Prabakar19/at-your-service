from typing import Dict

from fastapi import APIRouter

from model.customer import Customer
from service.customer_service import CustomerService

router = APIRouter(
    prefix="/customer",
    tags=["customer"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{customer_id}")
async def get_customer(customer_id: str):
    customer_service = CustomerService()
    return await customer_service.get_customer(customer_id)


@router.post("/")
async def add_customer(customer: Customer):
    customer_service = CustomerService()
    await customer_service.add_customer(customer)
    return {'data': 'Customer added successfully'}


@router.put("/")
async def update_customer(customer: Customer):
    customer_service = CustomerService()
    await customer_service.update_customer(customer)
    return {'data': 'Customer details updated successfully'}


@router.post("/login")
async def get_customer(login_details: Dict[str, str]):
    customer_service = CustomerService()
    customer_details = await customer_service.customer_login(login_details)
    return customer_details if customer_details else {'data': 'No customer found'}
