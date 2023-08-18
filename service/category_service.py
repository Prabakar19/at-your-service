from dao.category_dao import CategoryDao
from model.category import Category


class CategoryService:

    async def add_category(self, category: Category):
        await CategoryDao.add_category(category.model_dump())

    async def get_category_by_name(self, cat_name: str):
        category = await CategoryDao.get_category_name(cat_name)
        return category if category else {'data': 'Category not Found'}

    async def get_category_by_id(self, cat_id: str):
        category = await CategoryDao.get_category_by_id(cat_id)
        return category if category else {'data': 'Category not Found'}

    async def get_all_categories(self):
        categories = await CategoryDao.get_all_categories()
        for category in categories:
            category['categoryName'] = category.pop('category_name')
            category['categoryId'] = category.pop('category_id')
            category['categoryPic'] = category.pop('category_pic')
        return categories if categories else {'data': 'No category Found'}
