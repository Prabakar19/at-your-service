from typing import Dict, Any, List

from fastapi import APIRouter

from service.transaction_service import TransactionService

transaction_router = APIRouter(
    prefix="/transaction",
    tags=["Transaction APIs"],
    responses={404: {"description": "Not found"}},
)


@transaction_router.post("/list")
async def add_transaction_list(transactions: List[Dict[str, Any]]):
    transaction_service = TransactionService()
    await transaction_service.add_transaction_list(transactions)
    return {'data': 'Transaction saved successfully!'}


@transaction_router.get("/customer/{customer_id}")
async def get_all_cust_transaction(customer_id: str):
    transaction_service = TransactionService()
    return await transaction_service.get_all_cust_transaction(customer_id)


@transaction_router.put("/rating/{transaction_id}")
async def get_all_cust_transaction(transaction_id: str, rating: Dict[str, Any]):
    transaction_service = TransactionService()
    return await transaction_service.update_rating(transaction_id, rating)

