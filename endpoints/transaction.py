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


@router.get("/customer/{customer_id}")
async def get_all_cust_transaction(customer_id: str):
    transaction_service = TransactionService()
    return await transaction_service.get_all_cust_transaction(customer_id)


# @router.put("/rating/{transaction_id}/{rating}")
# async def get_all_cust_transaction(transaction_id: str, rating: int):
#     transaction_service = TransactionService()
#     return await transaction_service.get_all_cust_transaction(transaction_id)

