from typing import List
from uuid import UUID

from pydantic import BaseModel
from model.transaction import Transaction


class Billing(BaseModel):
    billing_id: UUID
    cost: float
    gst: float
    mrp_cost: float
    total_cost: float
    customer_id: UUID
    service_provider_id: UUID
    transactions: List[Transaction]
