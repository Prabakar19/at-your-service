from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select

from service.portgresql.postgres_provider import DbBase, PostgresProvider


class AddressDao(DbBase):
    __tablename__ = 'address'
    address_id = Column(String, name='customer_id', primary_key=True)
    house_address = Column(String, name='house_address')
    area = Column(String, name='area')
    city = Column(String, name='city')
    state = Column(String, name='state')
    country = Column(String, name='country')
    pincode = Column(String, name='pincode')

    @classmethod
    async def add_address(cls, address):
        query = [sa.insert(cls).values(address)]
        await PostgresProvider.execute(query)

    @classmethod
    async def get_address_by_id(cls, address_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.address_id == address_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_address_by_customer_id(cls, customer_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.customer_id == customer_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_address_by_service_provider_id(cls, service_provider_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.service_provider_id == service_provider_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def update_address(cls, address):
        query = [sa.update(cls).where(cls.name == address['address_id']).values(address)]
        await PostgresProvider.execute(query)
