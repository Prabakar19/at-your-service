from typing import Dict

from dao.customer_dao import CustomerDao
from model.customer import Customer
from service.address_service import AddressService


class CustomerService:

    async def get_customer(self, customer_id: str):
        customer = await CustomerDao.get_customer_by_id(customer_id)
        return customer

    async def add_customer(self, customer: Customer):
        customer = customer.model_dump()
        cust_address = customer.pop('address', None)
        cust_address['customer_id'] = customer['customer_id']

        # TODO: add encryption logic to encrypt password
        await CustomerDao.add_customer(customer, cust_address)

    async def update_customer(self, customer: Customer):
        customer = customer.model_dump()
        cust_address = customer.pop('address', None)
        await CustomerDao.update_customer(customer)
        if cust_address:
            cust_address['customer_id'] = customer['customer_id']
            await AddressService().update_address(cust_address)

    async def customer_login(self, login_details: Dict[str, str]):
        customer = await CustomerDao.get_customer_by_email(login_details['email_id'])
        if customer:
            password = customer.get('password')
            if password == login_details['password']:
                return customer

        return None
