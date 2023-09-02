from typing import Dict, Any, List

from fastapi import APIRouter

from service.billing_service import BillingService
from service.transaction_service import TransactionService

router = APIRouter(
    prefix="/transaction",
    tags=["Transaction"],
    responses={404: {"description": "Not found"}},
)


@router.post("/list")
async def add_transaction_list(transactions: List[Dict[str, Any]]):
    transaction_service = TransactionService()
    await transaction_service.add_transaction_list(transactions)
    return {'data': 'Transaction saved successfully!'}

