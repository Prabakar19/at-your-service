from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from dao.transaction_dao import TransactionDao
from service.portgresql.postgres_provider import DbBase, PostgresProvider


class ServiceDao(DbBase):
    __tablename__ = 'service'
    service_id = Column(String, name='service_id', primary_key=True)
    service_name = Column(String, name='service_name')
    cost = Column(Float, name='cost')
    discount = Column(Float, name='discount')
    discounted_cost = Column(Float, name='discounted_cost')
    discount_availability = Column(Boolean, name='discount_availability')
    details = Column(String, name='details')
    warranty = Column(Float, name='warranty')
    service_provider_id = Column(String, ForeignKey('serviceprovider.service_provider_id'), name='service_provider_id')
    category_id = Column(String, ForeignKey('category.category_id'), name='category_id')
    service_ratings = Column(Float, name='service_ratings')
    rating = Column(Float, name='rating')
    service_pic = Column(String, name='service_ratings')

    category = relationship('CategoryDao', back_populates='cat_service')
    service_provider = relationship('ServiceProviderDao', back_populates='sp_service')

    service_transaction = relationship('TransactionDao', order_by=TransactionDao.service_id, back_populates='service')

    @classmethod
    async def add_service(cls, service):
        query = [sa.insert(cls).values(service)]
        await PostgresProvider.execute_transaction(query)

    @classmethod
    async def get_service_by_id(cls, service_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.service_id == service_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_service_by_service_provider_id(cls, service_provider_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.service_provider_id == service_provider_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_service_by_category_id(cls, category_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.service_provider_id == category_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def update_category(cls, service):
        query = [sa.update(cls).where(cls.service_id == service['service_id']).values(service)]
        await PostgresProvider.execute(query)
