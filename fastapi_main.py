import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from endpoints.meta_endpoints import meta_router
from endpoints.customer import customer_router
from endpoints.category import category_router
from endpoints.service import service_router
from endpoints.billing import billing_router
from endpoints.transaction import transaction_router
from endpoints.cart import cart_router
from endpoints.service_provider import sp_router


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

    application.include_router(prefix=prefix, router=customer_router)
    application.include_router(prefix=prefix, router=sp_router)
    application.include_router(prefix=prefix, router=category_router)
    application.include_router(prefix=prefix, router=service_router)
    application.include_router(prefix=prefix, router=cart_router)
    application.include_router(prefix=prefix, router=billing_router)
    application.include_router(prefix=prefix, router=transaction_router)
    application.include_router(prefix=prefix, router=meta_router)
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run('fastapi_main:app', host="localhost", port=9098)
