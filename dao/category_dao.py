from typing import Any, Dict, List

import sqlalchemy as sa
from sqlalchemy import Column, String, select
from sqlalchemy.orm import relationship

from dao.service_dao import ServiceDao
from service.portgresql.postgres_provider import DbBase, PostgresProvider


class CategoryDao(DbBase):
    __tablename__ = 'category'
    billing_id = Column(String, name='category_id', primary_key=True)
    category_name = Column(String, name='category_name')
    category_pic = Column(String, name='category_pic')

    # cat_service = relationship('ServiceDao', order_by=ServiceDao.service_id, back_populates='service_cat')

    @classmethod
    async def add_category(cls, category):
        query = [sa.insert(cls).values(category)]
        await PostgresProvider.execute_transaction(query)

    @classmethod
    async def get_category_by_id(cls, category_id: str) -> Dict[str, Any]:
        query = select(cls).where(cls.category_id == category_id)
        cat = await PostgresProvider.get_list(query)
        return cat[0] if cat else None

    @classmethod
    async def get_category_name(cls, category_name: str) -> Dict[str, Any]:
        query = select(cls).where(cls.category_name == category_name)
        cat = await PostgresProvider.get_list(query)
        return cat[0] if cat else None

    @classmethod
    async def get_all_categories(cls) -> List[Dict[str, Any]]:
        query = select(cls)
        categories = await PostgresProvider.get_list(query)
        return categories

    @classmethod
    async def update_category(cls, category):
        query = [sa.update(cls).where(cls.category_id == category['category_id']).values(category)]
        await PostgresProvider.execute(query)
