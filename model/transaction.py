from datetime import datetime

from pydantic import BaseModel
from uuid import UUID


class Transaction(BaseModel):
    transaction_id: UUID
    billing_id: UUID
    service_id: UUID
    customer_id: UUID
    transaction_time: datetime
    transaction_amount: float
    transaction_rating: float
    original_cost: float
