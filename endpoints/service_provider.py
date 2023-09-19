from typing import Dict

from fastapi import APIRouter

from model.service_provider import ServiceProvider
from service.service_provider_service import ServiceProviderService

sp_router = APIRouter(
    prefix="/serviceprovider",
    tags=["Service Provider APIs"],
    responses={404: {"description": "Not found"}},
)


@sp_router.get("/{service_provider_id}")
async def get_service_provider(service_provider_id: str):
    service_provider_service = ServiceProviderService()
    return await service_provider_service.get_service_provider(service_provider_id)


@sp_router.post("/")
async def add_service_provider(service_provider: ServiceProvider):
    service_provider_service = ServiceProviderService()
    await service_provider_service.add_service_provider(service_provider)
    return {'data': 'Service Provider added successfully'}


@sp_router.put("/")
async def update_service_provider(service_provider: ServiceProvider):
    service_provider_service = ServiceProviderService()
    await service_provider_service.update_service_provider(service_provider)
    return {'data': 'Service Provider details updated successfully'}


@sp_router.post("/login")
async def login_service_provider(login_details: Dict[str, str]):
    service_provider_service = ServiceProviderService()
    sp_details = await service_provider_service.service_provider_login(login_details)
    return sp_details if sp_details else {'data': 'Service Provider not found'}
