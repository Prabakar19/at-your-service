

class CustomerService:
    CUSTOMERS = {1: 'praba', 2: 'priyanka', 3: 'surya'}

    def get_customer(self, customer_id: int):
        return self.CUSTOMERS.get(customer_id, 'No Customer Found')
