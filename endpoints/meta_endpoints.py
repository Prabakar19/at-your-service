from typing import Dict, List, Set

from fastapi import APIRouter

from service.service_provider_service import ServiceProviderService

meta_router = APIRouter(
    prefix="/meta_api",
    tags=["Meta APIs"],
    responses={404: {"description": "Not found"}},
)


@meta_router.get("/cities")
async def get_sp_cities() -> Set[str]:
    sp_service = ServiceProviderService()
    return await sp_service.get_sp_cities()

