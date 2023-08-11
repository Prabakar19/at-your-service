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


# TODO: fix add customer
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
