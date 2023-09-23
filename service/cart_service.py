import datetime
from typing import Any, Dict, List

from dao.cart_dao import CartDao
from dao.service_dao import ServiceDao
from service.service import ServiceService


class CartService:

    async def add_service_to_cart(self, details: Dict[str, Any]):

        if await(self.is_service_already_available(details)):
            return {'data': 'Service is already available in cart'}

        details['created_time'] = datetime.datetime.now()
        await CartDao.add_service_in_cart(details)
        return {'data': 'service added to cart successfully!'}

    async def get_user_cart(self, customer_id: str) -> List[Dict[str, Any]]:
        cart_list = await CartDao.get_cart_by_cust_id(customer_id)
        if not cart_list:
            return []

        service_ids = [item['service_id'] for item in cart_list]
        service_list = await ServiceDao.get_service_list_by_ids(service_ids)
        for service in service_list:
            ServiceService.transform_services_for_ui(service)

        return service_list

    async def remove_service(self, customer_id: str, service_id: str):
        await CartDao.delete_cart(customer_id, service_id)

    @staticmethod
    async def is_service_already_available(details):
        cart = await CartDao.get_cart_by_cust_id_n_service(details['customer_id'], details['service_id'])
        return True if cart else False
