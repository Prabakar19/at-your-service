from fastapi import APIRouter

from model.service import Service
from service.service import ServiceService

router = APIRouter(
    prefix="/service",
    tags=["service"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def add_service(service: Service):
    srvc = ServiceService()
    await srvc.add_service(service)
    return {'data': 'Service added successfully'}


@router.get('/{category_id}/{location}')
async def get_services_based_on_location(category_id: str, location: str):
    service = ServiceService()
    service_list = await service.get_service_list_by_location_category(category_id, location)
    return service_list
