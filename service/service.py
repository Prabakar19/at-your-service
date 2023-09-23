from typing import Dict

from dao.service_dao import ServiceDao
from dao.service_provider_dao import ServiceProviderDao
from model.service import Service, ServiceRequest
from utils.id_generator import IdGenerator


class ServiceService:

    async def add_service(self, service: dict):
        service['serviceId'] = IdGenerator.generate_uuid()
        service = self.transform_services(service)
        if service['discount_availability']:
            service['discounted_cost'] = service['cost'] * service['discount'] * 0.01
        return await ServiceDao.add_service(service)

    async def get_service_list_by_location_category(self, category_id: str, location: str):
        services = await ServiceDao.get_services_by_cat_and_location(category_id, location)
        if not services:
            return []

        for service in services:
            self.transform_services_for_ui(service)

        return services

    async def get_service_provider_services(self, service_provider_id: str):
        services = await ServiceDao.get_service_by_service_provider_id(service_provider_id)
        if not services:
            return []

        for service in services:
            self.transform_services_for_ui(service)

        return services

    @staticmethod
    def transform_services_for_ui(service: Dict[str, any]):
        service['serviceId'] = service.pop('service_id')
        service['serviceName'] = service.pop('service_name')
        service['discountedCost'] = service.pop('discounted_cost')
        service['discountAvailability'] = service.pop('discount_availability')
        service['shortDescription'] = service.pop('short_description')
        service['serviceProviderId'] = service.pop('service_provider_id')
        service['categoryId'] = service.pop('category_id')
        service['servicePic'] = service.pop('service_pic')

    @staticmethod
    def transform_services(service: Dict[str, any]):
        service['service_id'] = service.pop('serviceId')
        service['service_name'] = service.pop('serviceName')
        service['discounted_cost'] = service.pop('discountedCost', 0)
        service['discount_availability'] = service.pop('discountAvailability')
        service['short_description'] = service.pop('shortDescription', '')
        service['service_provider_id'] = service.pop('serviceProviderId')
        service['category_id'] = service.pop('categoryId')
        service['service_pic'] = service.pop('servicePic', '')
        return service
