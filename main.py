from fastapi import FastAPI
from service.cutomer_serivce import CustomerService
app = FastAPI()


@app.get("/api/customer/{customer_id}")
def get_customer(customer_id: int):
    customer_service = CustomerService()
    return customer_service.get_customer(customer_id)
