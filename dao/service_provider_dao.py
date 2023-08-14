from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select, Float
from sqlalchemy.orm import relationship

from dao.address_dao import AddressDao
from dao.billing_dao import BillingDao
from dao.service_dao import ServiceDao
from service.portgresql.postgres_provider import DbBase, PostgresProvider


class ServiceProviderDao(DbBase):
    __tablename__ = 'serviceprovider'
    service_provider_id = Column(String, name='service_provider_id', primary_key=True)
    company_name = Column(String, name='company_name')
    owner_name = Column(String, name='owner_name')
    email_id = Column(String, name='email_id')
    contact_number = Column(String, name='contact_number')
    password = Column(String, name='password')
    sp_rating = Column(Float, name='sp_rating')

    sp_address = relationship('AddressDao', order_by=AddressDao.address_id, back_populates='service_provider')
    sp_service = relationship('ServiceDao', order_by=ServiceDao.service_id, back_populates='service_provider')
    sp_billing = relationship('BillingDao', order_by=BillingDao.billing_id, back_populates='service_provider')

    @classmethod
    async def add_service_provider(cls, service_provider, address):
        query = [sa.insert(cls).values(service_provider)]
        await PostgresProvider.execute_transaction(query)

        if address:
            query1 = [sa.insert(AddressDao).values(address)]
            await PostgresProvider.execute_transaction(query1)

    @classmethod
    async def get_service_provider_by_id(cls, service_provider_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.service_provider_id == service_provider_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_service_provider_by_name(cls, company_name: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.company_name == company_name)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def update_service_provider(cls, service_provider):
        query = [sa.update(cls).where(cls.service_provider_id == service_provider['service_provider_id'])
                 .values(service_provider)]
        await PostgresProvider.execute_transaction(query)
