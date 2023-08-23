from typing import Dict

from fastapi import APIRouter

from model.category import Category
from service.category_service import CategoryService

router = APIRouter(
    prefix="/category",
    tags=["category"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def add_category(category: Category):
    category_service = CategoryService()
    await category_service.add_category(category)
    return {'data': 'Category added successfully'}


@router.get("/all")
async def get_all_category():
    customer_service = CategoryService()
    return await customer_service.get_all_categories()


@router.get("/all/{city_name}")
async def get_all_category_by_city(city_name: str):
    customer_service = CategoryService()
    return await customer_service.get_all_categories_by_city(city_name)


@router.get("/{category_id}")
async def get_category(category_id: str):
    customer_service = CategoryService()
    return await customer_service.get_category_by_id(category_id)


@router.get("/name/{category_name}")
async def get_category_by_name(category_name: str):
    customer_service = CategoryService()
    return await customer_service.get_category_by_name(category_name)
