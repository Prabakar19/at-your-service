from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select

from service.portgresql.postgres_provider import DbBase, PostgresProvider


class CustomerDao(DbBase):
    __tablename__ = 'customer'
    customer_id = Column(String, name='customer_id', primary_key=True)
    customer_name = Column(String, name='customer_name')
    first_name = Column(String, name='first_name')
    last_name = Column(String, name='last_name')
    email_id = Column(String, name='email_id')
    phone_number = Column(String, name='phone_number')
    password = Column(String, name='password')

    # address = relationship('Address')

    @classmethod
    async def add_customer(cls, customer):
        query = [sa.insert(CustomerDao).values(customer)]
        await PostgresProvider.execute(query)

    @classmethod
    async def get_customer_by_name(cls, customer_name: str) -> List[Dict[str, Any]]:
        query = select(CustomerDao).where(cls.customer_name == customer_name)
        return await PostgresProvider.execute(query)

    @classmethod
    async def get_customer_by_id(cls, customer_id: str) -> List[Dict[str, Any]]:
        query = select(CustomerDao).where(cls.customer_id == customer_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_all_customer(cls) -> List[Dict[str, Any]]:
        query = select(CustomerDao)
        return await PostgresProvider.execute(query)

    @classmethod
    async def update_customer(cls, customer):
        query = [sa.update(CustomerDao).where(cls.name == customer['name']).values(customer)]
        await PostgresProvider.execute(query)
