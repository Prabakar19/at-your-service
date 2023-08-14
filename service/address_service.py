from typing import Any, Dict

from dao.address_dao import AddressDao
from model.address import Address


class AddressService:

    async def get_address(self, address_id: str):
        address = await AddressDao.get_address_by_id(address_id)
        return address

    async def update_address(self, address: Dict[str, Any]):
        await AddressDao.update_address(address)

