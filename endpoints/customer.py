from fastapi import APIRouter

from service.cutomer_serivce import CustomerService

router = APIRouter(prefix="/customer", tags=["customer"], responses={404: {"description": "Not found"}})


@router.get("/{customer_id}")
async def get_customer(customer_id: str):
    customer_service = CustomerService()
    return await customer_service.get_customer(customer_id)
