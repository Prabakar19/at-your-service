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

    sp_address = relationship('AddressDao', order_by=AddressDao.address_id, back_populates='address_sp')
    sp_service = relationship('ServiceDao', order_by=ServiceDao.service_id, back_populates='service_sp')
    sp_billing = relationship('BillingDao', order_by=BillingDao.billing_id, back_populates='billing_sp')

    @classmethod
    async def add_service_provider(cls, service_provider, address):
        query = [sa.insert(cls).values(service_provider)]
        await PostgresProvider.execute_transaction(query)

        if address:
            query1 = [sa.insert(AddressDao).values(address)]
            await PostgresProvider.execute_transaction(query1)

    @classmethod
    async def get_service_provider_by_id(cls, service_provider_id: str) -> Dict[str, Any]:
        query = select(cls).where(cls.service_provider_id == service_provider_id)
        sp = await PostgresProvider.get_list(query)
        return sp[0] if sp else None

    @classmethod
    async def get_service_provider_by_email(cls, email_id: str) -> Dict[str, Any]:
        query = select(cls).where(cls.email_id == email_id)
        sp = await PostgresProvider.get_list(query)
        return sp[0] if sp else None

    @classmethod
    async def get_all_sp_cities(cls) -> List[Dict[str, str]]:
        query = select(AddressDao.city).join(cls.sp_address).order_by(cls.service_provider_id, AddressDao.service_provider_id)
        city_list = await PostgresProvider.get_list(query)
        return city_list

    @classmethod
    async def update_service_provider(cls, service_provider):
        query = [sa.update(cls).where(cls.service_provider_id == service_provider['service_provider_id'])
                 .values(service_provider)]
        await PostgresProvider.execute_transaction(query)

    @classmethod
    async def get_sp_by_city(cls, city) -> List[Dict[str, str]]:
        query = select(cls.service_provider_id).join(cls.sp_address).order_by(
            cls.service_provider_id, AddressDao.service_provider_id).where(AddressDao.city == city)
        sp_ids = await PostgresProvider.get_list(query)
        return sp_ids
