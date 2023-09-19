from fastapi import APIRouter

from service.billing_service import BillingService

billing_router = APIRouter(
    prefix="/billing",
    tags=["Billing APIs"],
    responses={404: {"description": "Not found"}},
)


@billing_router.post("")
async def add_billing(billing: dict):
    billing_service = BillingService()
    return await billing_service.add_billing(billing)

