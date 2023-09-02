from fastapi import APIRouter

router = APIRouter(
    prefix="/billing",
    tags=["Billing"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def add_billing(billing):
    pass
