from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select, Float, Boolean

from service.portgresql.postgres_provider import DbBase, PostgresProvider


class ServiceProviderDao(DbBase):
    __tablename__ = 'serviceprovider'
    service_provider_id = Column(String, name='service_provider_id', primary_key=True)
    company_name = Column(String, name='company_name')
    owner_name = Column(Float, name='owner_name')
    email_id = Column(Float, name='email_id')
    contact_number = Column(Float, name='contact_number')
    password = Column(Boolean, name='password')
    sp_rating = Column(String, name='sp_rating')

    @classmethod
    async def add_service_provider(cls, service_provider):
        query = [sa.insert(cls).values(service_provider)]
        await PostgresProvider.execute_transaction(query)

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
        query = [sa.update(cls).where(cls.service_provider_id == service_provider['service_provider_id']).values(service_provider)]
        await PostgresProvider.execute(query)
