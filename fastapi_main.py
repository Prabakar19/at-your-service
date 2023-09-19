import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from endpoints import customer, category, meta_endpoints, service, cart, billing, transaction, address
from endpoints import service_provider


def get_application() -> FastAPI:
    prefix = '/api'
    """ Configure, start and return the application """
    application = FastAPI()

    origins = ["http://localhost", "http://localhost:9098"]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(prefix=prefix, router=customer.router)
    application.include_router(prefix=prefix, router=service_provider.router)
    application.include_router(prefix=prefix, router=category.router)
    application.include_router(prefix=prefix, router=service.router)
    application.include_router(prefix=prefix, router=cart.router)
    application.include_router(prefix=prefix, router=billing.router)
    application.include_router(prefix=prefix, router=transaction.router)
    application.include_router(prefix=prefix, router=address.router)
    application.include_router(prefix=prefix, router=meta_endpoints.router)
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run('fastapi_main:app', host="localhost", port=9098)
