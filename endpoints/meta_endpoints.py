from typing import Dict

from fastapi import APIRouter

from model.customer import Customer
from model.service_provider import ServiceProvider
from service.customer_service import CustomerService
from service.service_provider_service import ServiceProviderService

router = APIRouter(
    prefix="/meta_api",
    tags=["meta_api"],
    responses={404: {"description": "Not found"}},
)


@router.get("/cities")
async def get_sp_cities():
    sp_service = ServiceProviderService()
    return await sp_service.get_sp_cities()

