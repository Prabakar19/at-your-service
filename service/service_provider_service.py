from dao.service_provider_dao import ServiceProviderDao
from model.service_provider import ServiceProvider
from service.address_service import AddressService


class ServiceProviderService:

    async def get_service_provider(self, service_provider_id: str):
        service_provider = await ServiceProviderDao.get_service_provider_by_id(service_provider_id)
        return service_provider

    async def add_service_provider(self, service_provider: ServiceProvider):
        service_provider = service_provider.model_dump()
        service_provider_address = service_provider.pop('address', None)
        service_provider_address['service_provider_id'] = service_provider['service_provider_id']

        await ServiceProviderDao.add_service_provider(service_provider, service_provider_address)

    async def update_service_provider(self, service_provider: ServiceProvider):
        service_provider = service_provider.model_dump()
        service_provider_address = service_provider.pop('address', None)
        await ServiceProviderDao.update_service_provider(service_provider)

        if service_provider_address:
            service_provider_address['service_provider_id'] = service_provider['service_provider_id']
            await AddressService().update_address(service_provider_address)
