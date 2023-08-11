from dao.customer_dao import CustomerDao
from model.customer import Customer


class CustomerService:

    async def get_customer(self, customer_id: str):
        customer = await CustomerDao.get_customer_by_id(customer_id)
        return customer

    async def add_customer(self, customer: Customer):
        customer = customer.model_dump()
        cust_address = customer.pop('address', None)
        cust_address['customer_id'] = customer['customer_id']

        await CustomerDao.add_customer(customer, cust_address)


    async def update_customer(self, customer: Customer):
        await CustomerDao.update_customer(customer)
