from typing import Dict, List

from dao.address_dao import AddressDao
from dao.category_dao import CategoryDao
from dao.service_dao import ServiceDao
from dao.service_provider_dao import ServiceProviderDao
from model.category import Category


class CategoryService:

    async def add_category(self, category: Category):
        await CategoryDao.add_category(category.model_dump())

    async def get_category_by_name(self, cat_name: str):
        category = await CategoryDao.get_category_by_name(cat_name)
        return self.transform_category(category) if category else {'data': 'Category not Found'}

    async def get_category_by_id(self, cat_id: str):
        category = await CategoryDao.get_category_by_id(cat_id)
        return category if category else {'data': 'Category not Found'}

    async def get_all_categories(self):
        categories = await CategoryDao.get_all_categories()
        for category in categories:
            category = self.transform_category(category)
        return categories if categories else {'data': 'No category Found'}

    async def get_all_categories_by_city(self, city_name) -> List[str]:
        sp_ids = await ServiceProviderDao.get_sp_by_city(city_name)
        if sp_ids:
            sp_ids = [sp_id['service_provider_id'] for sp_id in sp_ids]
            category_list = await ServiceDao.get_category_list_by_sp_ids(sp_ids)
            category_ids = [category['category_id'] for category in category_list]
            category_list = await CategoryDao.get_category_name_by_ids(category_ids)
            return [cat['category_name'] for cat in category_list]
        return []

    @staticmethod
    def transform_category(category: Dict[str, str]) -> Dict[str, str]:
        category['categoryName'] = category.pop('category_name')
        category['categoryId'] = category.pop('category_id')
        category['categoryPic'] = category.pop('category_pic')
        return category
