from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select, Float, Boolean, TIMESTAMP

from service.portgresql.postgres_provider import DbBase, PostgresProvider


class TransactionDao(DbBase):
    __tablename__ = 'transaction'
    transaction_id = Column(String, name='transaction_id', primary_key=True)
    billing_id = Column(String, name='billing_id')
    service_id = Column(String, name='service_id')
    transaction_time = Column(TIMESTAMP, name='transaction_time')
    transaction_amount = Column(Float, name='transaction_amount')
    original_cost = Column(Float, name='original_cost')

    @classmethod
    async def add_transaction(cls, transaction):
        query = [sa.insert(cls).values(transaction)]
        await PostgresProvider.execute_transaction(query)

    @classmethod
    async def get_transaction_by_id(cls, transaction_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.transaction_id == transaction_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_transaction_by_billing_id(cls, billing_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.billing_id == billing_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_transaction_by_service_id(cls, service_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.service_id == service_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_transaction_by_customer_id(cls, customer_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.customer_id == customer_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def update_transaction(cls, transaction):
        query = [sa.update(cls).where(cls.transaction_id == transaction['transaction_id']).values(transaction)]
        await PostgresProvider.execute(query)
