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
