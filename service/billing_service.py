from typing import Any, Dict

from dao.billing_dao import BillingDao
from utils.id_generator import IdGenerator


class BillingService:

    async def add_billing(self, billing) -> Dict[str, Any]:
        billing['customer_id'] = billing.pop('customerId')
        billing['total_cost'] = billing.pop('totalCost')
        billing['service_provider_id'] = billing.pop('serviceProviderId')
        billing['billing_id'] = IdGenerator.generate_uuid()
        billing.pop('type', None)
        return self.billing_for_ui(await BillingDao.add_billing(billing))

    @staticmethod
    def billing_for_ui(billing: Dict[str, Any]):
        billing['billingId'] = billing.pop('billing_id')
        billing['customerId'] = billing.pop('customer_id')
        billing['serviceProviderId'] = billing.pop('service_provider_id')
        billing['totalCost'] = billing.pop('total_cost')
        billing['mrpCost'] = billing.pop('mrp_cost')
        return billing

