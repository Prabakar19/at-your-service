from dao.customer_dao import CustomerDao


class CustomerService:
    CUSTOMERS = {'1': 'praba', '2': 'priyanka', '3': 'surya'}

    async def get_customer(self, customer_id: str):
        # customer = await CustomerDao.get_customer_by_id(customer_id)
        customer = self.CUSTOMERS.get(customer_id, 'No Customer Found')
        return customer
