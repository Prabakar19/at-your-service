from typing import Dict, Any

from fastapi import APIRouter

from service.billing_service import BillingService

router = APIRouter(
    prefix="/billing",
    tags=["Billing"],
    responses={404: {"description": "Not found"}},
)


@router.post("")
async def add_billing(billing: Dict[str, Any]):
    billing_service = BillingService()
    return await billing_service.add_billing(billing)

