import copy
from typing import Dict

from dao.service_dao import ServiceDao
from utils.id_generator import IdGenerator


class ServiceService:

    async def add_service(self, service: dict):
        service['serviceId'] = IdGenerator.generate_uuid()
        service = self.transform_services(service)
        self.calculate_discount_amount(service)
        service = await ServiceDao.add_service(service)
        self.transform_services_for_ui(service)
        return service

    async def modify_service(self, service_request: dict):
        service = copy.deepcopy(service_request)
        service = self.transform_services(service)
        self.calculate_discount_amount(service)
        await ServiceDao.update_service(service)
        service_request['discountedCost'] = service['discounted_cost']
        return service_request

    @staticmethod
    def calculate_discount_amount(service: dict):
        service['discounted_cost'] = service['cost']
        if service['discount_availability'] and service['discount'] != 0:
            service['discounted_cost'] = service['cost'] - (service['cost'] * service['discount'] * 0.01)

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

    async def remove_service(self, service_id: str):
        await ServiceDao.delete_service_by_id(service_id)
        return service_id

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
