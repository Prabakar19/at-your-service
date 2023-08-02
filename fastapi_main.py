import uvicorn
from fastapi import FastAPI

from endpoints import customer


def get_application() -> FastAPI:
    """ Configure, start and return the application """
    application = FastAPI()

    application.include_router(customer.router)
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run('fastapi_main:app', host="localhost", port=9098)
