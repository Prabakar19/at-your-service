from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select, TIMESTAMP, delete

from service.portgresql.postgres_provider import DbBase, PostgresProvider


class CartDao(DbBase):
    __tablename__ = 'usercart'
    customer_id = Column(String, name='customer_id', primary_key=True)
    service_id = Column(String, name='service_id', primary_key=True)
    created_time = Column(TIMESTAMP, name='created_time')

    @classmethod
    async def add_service_in_cart(cls, details):
        query = [sa.insert(cls).values(details)]
        await PostgresProvider.execute_transaction(query)

    @classmethod
    async def get_cart_by_cust_id_n_service(cls, cust_id: str, service_id) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.customer_id == cust_id).where(cls.service_id == service_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_cart_by_cust_id(cls, cust_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.customer_id == cust_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def delete_cart(cls, customer_id: str, service_id: str):
        query = delete(cls).where(cls.customer_id == customer_id).where(cls.service_id == service_id)
        await PostgresProvider.execute(query)
