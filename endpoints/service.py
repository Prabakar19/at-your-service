from fastapi import APIRouter

from model.service import ServiceRequest
from service.service import ServiceService

service_router = APIRouter(
    prefix="/service",
    tags=["Service APIs"],
    responses={404: {"description": "Not found"}},
)


@service_router.post("")
async def add_service(service: ServiceRequest):
    srvc = ServiceService()
    return await srvc.add_service(service.model_dump())


@service_router.get('/serviceprovider/{service_provider_id}')
async def get_services_based_on_location(service_provider_id: str):
    service = ServiceService()
    service_list = await service.get_service_provider_services(service_provider_id)
    return service_list


@service_router.get('/{category_id}/{location}')
async def get_services_based_on_location(category_id: str, location: str):
    service = ServiceService()
    service_list = await service.get_service_list_by_location_category(category_id, location)
    return service_list


@service_router.delete('/id/{service_id}')
async def get_services_based_on_location(service_id: str):
    service = ServiceService()
    return await service.remove_service(service_id)
