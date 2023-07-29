from dao.customer_dao import CustomerDao


class CustomerService:

    async def get_customer(self, customer_id: str):
        customer = await CustomerDao.get_customer_by_id(customer_id)
        return customer
