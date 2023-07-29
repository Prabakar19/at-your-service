import uvicorn
from fastapi import FastAPI

from service.cutomer_serivce import CustomerService

app = FastAPI()


@app.get("/api/customer/{customer_id}")
async def get_customer(customer_id: str):
    customer_service = CustomerService()
    return await customer_service.get_customer(customer_id)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9098)
