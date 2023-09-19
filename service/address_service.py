from typing import Any, Dict

from dao.address_dao import AddressDao
from model.address import Address


class AddressService:

    async def get_address(self, address_id: str):
        address = await AddressDao.get_address_by_id(address_id)
        return address

    async def update_address(self, address: Dict[str, Any]):
        address['address_id'] = address.pop('addressId')
        address['house_address'] = address.pop('houseAddress')
        await AddressDao.update_address(address)

    async def get_customer_address(self, customer_id: str):
        customer_address = await AddressDao.get_address_by_customer_id(customer_id)
        customer_address = self.change_dict_for_ui(customer_address)
        customer_address.pop('serviceProviderId', None)
        return customer_address

    @staticmethod
    def change_dict_for_ui(address: dict):
        address['addressId'] = address.pop('address_id')
        address['houseAddress'] = address.pop('house_address')
        address['serviceProviderId'] = address.pop('service_provider_id')
        address['customerId'] = address.pop('customer_id')
        return address
