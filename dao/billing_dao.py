from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select, Float

from service.portgresql.postgres_provider import DbBase, PostgresProvider


class BillingDao(DbBase):
    __tablename__ = 'billing'
    billing_id = Column(String, name='billing_id', primary_key=True)
    cost = Column(Float, name='cost')
    gst = Column(Float, name='gst')
    mrp_cost = Column(Float, name='mrp_cost')
    total_cost = Column(Float, name='total_cost')
    customer_id = Column(String, name='customer_id')
    service_provider_id = Column(String, name='service_provider_id')

    @classmethod
    async def add_billing(cls, billing):
        query = [sa.insert(cls).values(billing)]
        await PostgresProvider.execute_transaction(query)

    @classmethod
    async def get_billing_by_id(cls, billing_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.billing_id == billing_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_billing_by_customer_id(cls, customer_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.customer_id == customer_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_billing_by_service_provider_id(cls, service_provider_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.service_provider_id == service_provider_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def update_address(cls, billing):
        query = [sa.update(cls).where(cls.billing_id == billing['billing_id']).values(billing)]
        await PostgresProvider.execute(query)
