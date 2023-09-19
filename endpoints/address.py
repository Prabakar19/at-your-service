from fastapi import APIRouter

from service.customer_service import CustomerService

router = APIRouter(
    prefix="/address",
    tags=["Address API"],
    responses={404: {"description": "Not found"}},
)


@router.put("")
async def update_customer_address(customer_address: dict):
    customer_service = CustomerService()
    return await customer_service.update_customer_address(customer_address)