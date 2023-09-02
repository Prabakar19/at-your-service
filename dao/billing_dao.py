from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select, Float, ForeignKey
from sqlalchemy.orm import relationship

from dao.transaction_dao import TransactionDao
from service.portgresql.postgres_provider import DbBase, PostgresProvider


class BillingDao(DbBase):
    __tablename__ = 'billing'
    billing_id = Column(String, name='billing_id', primary_key=True)
    cost = Column(Float, name='cost')
    gst = Column(Float, name='gst')
    mrp_cost = Column(Float, name='mrp_cost')
    total_cost = Column(Float, name='total_cost')
    customer_id = Column(String, ForeignKey('customer.customer_id'), name='customer_id')
    service_provider_id = Column(String, ForeignKey('serviceprovider.service_provider_id'), name='service_provider_id')

    billing_cust = relationship('CustomerDao', back_populates='cust_billing')
    billing_sp = relationship('ServiceProviderDao', back_populates='sp_billing')

    billing_transaction = relationship('TransactionDao', order_by=TransactionDao.service_id, back_populates='transaction_billing')

    @classmethod
    async def add_billing(cls, billing):
        query = [sa.insert(cls).values(billing)]
        await PostgresProvider.execute_transaction(query)
        return await cls.get_billing_by_id(billing['billing_id'])

    @classmethod
    async def get_billing_by_id(cls, billing_id: str) -> Dict[str, Any]:
        query = select(cls).where(cls.billing_id == billing_id)
        billing = await PostgresProvider.get_list(query)
        return billing[0] if billing else None

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
