import uvicorn
from fastapi import FastAPI

from endpoints import customer
from endpoints import service_provider


def get_application() -> FastAPI:
    """ Configure, start and return the application """
    application = FastAPI()

    application.include_router(customer.router)
    application.include_router(service_provider.router)
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run('fastapi_main:app', host="localhost", port=9098)
