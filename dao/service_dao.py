from typing import Any, Dict, List, Union

import sqlalchemy as sa
from sqlalchemy import Column, String, select, Float, Boolean, ForeignKey, delete
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
    rating = Column(Float, name='rating', default=0)
    service_pic = Column(String, name='service_pic')
    city = Column(String, name='city')
    short_description = Column(String, name='short_description')

    # TODO: fix this relationship issue of CategoryDao not locate
    # service_cat = relationship('CategoryDao', back_populates='cat_service')
    service_sp = relationship('ServiceProviderDao', back_populates='sp_service')
    service_transaction = relationship('TransactionDao', order_by=TransactionDao.service_id, back_populates='transaction_service')

    @classmethod
    async def add_service(cls, service):
        query = [sa.insert(cls).values(service)]
        await PostgresProvider.execute_transaction(query)
        return await cls.get_service_by_id(service['service_id'])

    @classmethod
    async def get_service_by_id(cls, service_id: str) -> Union[List[Dict[str, Any]], None]:
        query = select(cls).where(cls.service_id == service_id)
        service = await PostgresProvider.get_list(query)
        return service[0] if service else None

    @classmethod
    async def get_service_list_by_ids(cls, service_ids: List[str]) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.service_id.in_(service_ids))
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_service_by_service_provider_id(cls, service_provider_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.service_provider_id == service_provider_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_service_by_category_id(cls, category_id: str) -> List[Dict[str, Any]]:
        query = select(cls).where(cls.category_id == category_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_category_by_sp(cls, service_provider_id: str) -> List[Dict[str, Any]]:
        query = select(cls.category_id).where(cls.service_provider_id == service_provider_id)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_category_list_by_sp_ids(cls, sp_ids: List[str]):
        query = select(cls.category_id).where(cls.service_provider_id.in_(sp_ids))
        return await PostgresProvider.get_list(query)

    @classmethod
    async def get_services_by_cat_and_location(cls, cat_id: str, city: str):
        query = select(cls).where(cls.category_id == cat_id).where(cls.city == city)
        return await PostgresProvider.get_list(query)

    @classmethod
    async def update_category(cls, service):
        query = [sa.update(cls).where(cls.service_id == service['service_id']).values(service)]
        await PostgresProvider.execute(query)

    @classmethod
    async def update_rating(cls, service_id: str, rating: float):
        query = [sa.update(cls).where(cls.service_id == service_id).values({'rating': rating})]
        await PostgresProvider.execute_transaction(query)

    @classmethod
    async def delete_service_by_id(cls, service_id: str):
        query = delete(cls).where(cls.service_id == service_id)
        await PostgresProvider.execute(query)
