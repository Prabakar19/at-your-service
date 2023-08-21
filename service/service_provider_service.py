from typing import Dict, List, Set

from dao.service_provider_dao import ServiceProviderDao
from model.service_provider import ServiceProvider
from service.address_service import AddressService


class ServiceProviderService:

    async def get_service_provider(self, service_provider_id: str):
        service_provider = await ServiceProviderDao.get_service_provider_by_id(service_provider_id)
        return self.transform_sp(service_provider)

    async def add_service_provider(self, service_provider: ServiceProvider):
        service_provider = service_provider.model_dump()
        service_provider_address = service_provider.pop('address', None)
        service_provider_address['service_provider_id'] = service_provider['service_provider_id']

        # TODO: add encryption logic to encrypt password
        await ServiceProviderDao.add_service_provider(service_provider, service_provider_address)

    async def update_service_provider(self, service_provider: ServiceProvider):
        service_provider = service_provider.model_dump()
        service_provider_address = service_provider.pop('address', None)
        await ServiceProviderDao.update_service_provider(service_provider)

        if service_provider_address:
            service_provider_address['service_provider_id'] = service_provider['service_provider_id']
            await AddressService().update_address(service_provider_address)

    async def service_provider_login(self, login_details: Dict[str, str]):
        sp = await ServiceProviderDao.get_service_provider_by_email(login_details['email_id'])
        if sp:
            password = sp.get('password')
            if password == login_details['password']:
                return sp

        return None

    async def get_sp_cities(self) -> Set[str]:
        cities = await ServiceProviderDao.get_all_sp_cities()
        cities = set(city['city'] for city in cities)
        return cities

    @staticmethod
    def transform_sp(service_provider):
        service_provider['serviceProviderId'] = service_provider.pop('service_provider_id')
        service_provider['companyName'] = service_provider.pop('company_name')
        service_provider['ownerName'] = service_provider.pop('owner_name')
        service_provider['emailId'] = service_provider.pop('email_id')
        service_provider['phoneNum'] = service_provider.pop('contact_number')
        service_provider['spRating'] = service_provider.pop('sp_rating')
        return service_provider
