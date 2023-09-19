from fastapi import APIRouter

from service.cart_service import CartService

cart_router = APIRouter(
    prefix="/cart",
    tags=["Cart APIs"],
    responses={404: {"description": "Not found"}},
)


@cart_router.post("/")
async def add_to_cart(cart_details: dict):
    cart_service = CartService()
    return await cart_service.add_service_to_cart(cart_details)


@cart_router.get("/{customer_id}")
async def get_user_cart(customer_id: str):
    cart_service = CartService()
    return await cart_service.get_user_cart(customer_id)


@cart_router.delete("/{customer_id}/{service_id}")
async def remove_service(customer_id: str, service_id: str):
    cart_service = CartService()
    return await cart_service.remove_service(customer_id, service_id)
