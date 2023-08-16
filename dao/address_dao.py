from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select, ForeignKey
from sqlalchemy.orm import relationship

from service.portgresql.postgres_provider import DbBase, PostgresProvider


class AddressDao(DbBase):
    __tablename__ = 'address'
    address_id = Column(String, name='address_id', primary_key=True)
    house_address = Column(String, name='house_address')
    area = Column(String, name='area')
    city = Column(String, name='city')
    state = Column(String, name='state')
    country = Column(String, name='country')
    pincode = Column(String, name='pincode')
    customer_id = Column(String, ForeignKey('customer.customer_id'), name='customer_id')
    service_provider_id = Column(String, ForeignKey('serviceprovider.service_provider_id'), name='service_provider_id')

    address_cust = relationship('CustomerDao', back_populates='cust_address')
    address_sp = relationship('ServiceProviderDao', back_populates='sp_address')

    @classmethod
    async def add_address(cls, address):
        query = [sa.insert(cls).values(address)]
        await PostgresProvider.execute_transaction(query)

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
    async def update_address(cls, address: Dict[str, Any]):
        query = [sa.update(cls).where(cls.address_id == address['address_id']).values(address)]
        await PostgresProvider.execute_transaction(query)
