from typing import Dict, Any

from dao.address_dao import AddressDao
from dao.customer_dao import CustomerDao
from model.customer import Customer, CustomerRequest
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

    async def update_customer(self, customer: CustomerRequest):
        customer = customer.model_dump()
        cust_address = customer.pop('address', None)
        customer = self.transform_cust(customer)
        await CustomerDao.update_customer(customer)
        if cust_address:
            cust_address['customer_id'] = customer['customer_id']
            await AddressService().update_address(cust_address)
        return self.transform_cust_for_ui(customer)

    async def update_customer_address(self, cust_address: dict):
        cust_address['customer_id'] = cust_address['customerId']
        await AddressService().update_address(cust_address)
        return cust_address

    async def customer_login(self, login_details: Dict[str, str]):
        customer = await CustomerDao.get_customer_by_email(login_details['emailId'])
        if customer:
            password = customer.get('password')
            if password == login_details['password']:
                return self.transform_cust_for_ui(customer)

        return None

    @staticmethod
    def transform_cust_for_ui(customer: Dict[str, Any]):
        customer['customerId'] = customer.pop('customer_id')
        customer['customerName'] = customer.pop('customer_name')
        customer['firstName'] = customer.pop('first_name')
        customer['lastName'] = customer.pop('last_name')
        customer['emailId'] = customer.pop('email_id')
        customer['phoneNumber'] = customer.pop('phone_number')
        customer['password'] = customer.pop('password')
        return customer

    @staticmethod
    def transform_cust(customer: Dict[str, Any]):
        customer['customer_id'] = customer.pop('customerId')
        customer['customer_name'] = customer.pop('customerName')
        customer['first_name'] = customer.pop('firstName')
        customer['last_name'] = customer.pop('lastName')
        customer['email_id'] = customer.pop('emailId')
        customer['phone_number'] = customer.pop('phoneNumber')
        return customer
