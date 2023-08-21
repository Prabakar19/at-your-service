from typing import Dict

from dao.service_dao import ServiceDao
from dao.service_provider_dao import ServiceProviderDao
from model.service import Service


class ServiceService:

    async def add_service(self, service: Service):
        await ServiceDao.add_service(service.model_dump())

    async def get_service_list_by_location_category(self, category_id: str, location: str):
        services = await ServiceDao.get_services_by_cat_and_location(category_id, location)
        if not services:
            return []

        for service in services:
            self.transform_services(service)

        return services

    @staticmethod
    def transform_services(service: Dict[str, any]):
        service['serviceId'] = service.pop('service_id')
        service['serviceName'] = service.pop('service_name')
        service['discountedCost'] = service.pop('discounted_cost')
        service['discountAvailability'] = service.pop('discount_availability')
        service['shortDescription'] = service.pop('short_description')
        service['serviceProviderId'] = service.pop('service_provider_id')
        service['categoryId'] = service.pop('category_id')
        service['servicePic'] = service.pop('service_pic')
