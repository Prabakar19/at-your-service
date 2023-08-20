from dao.service_dao import ServiceDao
from model.service import Service


class ServiceService:

    async def add_service(self, service: Service):
        await ServiceDao.add_service(service.model_dump())