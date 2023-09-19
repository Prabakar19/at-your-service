from typing import Dict

from fastapi import APIRouter

from model.category import Category
from service.category_service import CategoryService

category_router = APIRouter(
    prefix="/category",
    tags=["Category APIs"],
    responses={404: {"description": "Not found"}},
)


@category_router.post("/")
async def add_category(category: Category):
    category_service = CategoryService()
    await category_service.add_category(category)
    return {'data': 'Category added successfully'}


@category_router.get("/all")
async def get_all_category():
    customer_service = CategoryService()
    return await customer_service.get_all_categories()


@category_router.get("/all/{city_name}")
async def get_all_category_by_city(city_name: str):
    customer_service = CategoryService()
    return await customer_service.get_all_categories_by_city(city_name)


@category_router.get("/{category_id}")
async def get_category(category_id: str):
    customer_service = CategoryService()
    return await customer_service.get_category_by_id(category_id)


@category_router.get("/name/{category_name}")
async def get_category_by_name(category_name: str):
    customer_service = CategoryService()
    return await customer_service.get_category_by_name(category_name)
