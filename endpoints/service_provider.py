from fastapi import APIRouter

from model.customer import Customer
from model.service_provider import ServiceProvider
from service.customer_service import CustomerService
from service.service_provider_service import ServiceProviderService

router = APIRouter(
    prefix="/serviceprovider",
    tags=["serviceprovider"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{service_provider_id}")
async def get_service_provider(service_provider_id: str):
    service_provider_service = ServiceProviderService()
    return await service_provider_service.get_service_provider(service_provider_id)


@router.post("/")
async def add_service_provider(service_provider: ServiceProvider):
    service_provider_service = ServiceProviderService()
    await service_provider_service.add_service_provider(service_provider)
    return {'data': 'Service Provider added successfully'}


@router.put("/")
async def update_service_provider(service_provider: ServiceProvider):
    service_provider_service = ServiceProviderService()
    await service_provider_service.update_service_provider(service_provider)
    return {'data': 'Service Provider details updated successfully'}