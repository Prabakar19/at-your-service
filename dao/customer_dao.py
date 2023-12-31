from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select
from sqlalchemy.orm import relationship

from dao.address_dao import AddressDao
from dao.billing_dao import BillingDao
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

    cust_address = relationship('AddressDao', order_by=AddressDao.address_id, back_populates='address_cust')
    cust_billing = relationship('BillingDao', order_by=BillingDao.billing_id, back_populates='billing_cust')

    @classmethod
    async def add_customer(cls, customer: Dict[str, Any], cust_address: Dict[str, Any]):
        query = [sa.insert(cls).values(customer)]
        await PostgresProvider.execute_transaction(query)

        if cust_address:
            query = [sa.insert(AddressDao).values(cust_address)]
            await PostgresProvider.execute_transaction(query)

    @classmethod
    async def get_customer_by_email(cls, email_id: str) -> Dict[str, Any]:
        query = select(cls).where(cls.email_id == email_id)
        customer = await PostgresProvider.get_list(query)
        return customer[0] if customer else None

    @classmethod
    async def get_customer_by_id(cls, customer_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.customer_id == customer_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_all_customer(cls) -> List[Dict[str, Any]]:
        query = select(cls)
        return await PostgresProvider.execute(query)

    @classmethod
    async def update_customer(cls, customer: Dict[str, Any]):
        query = [sa.update(cls).where(cls.customer_id == customer['customer_id']).values(customer)]
        await PostgresProvider.execute_transaction(query)
