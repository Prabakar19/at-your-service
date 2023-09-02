import datetime
from typing import List, Dict, Any

from dao.service_dao import ServiceDao
from dao.transaction_dao import TransactionDao


class TransactionService:

    async def add_transaction_list(self, transactions_list: List[Dict[str, Any]]):
        for transaction in transactions_list:
            transaction['transaction_time'] = datetime.datetime.now()
            transaction['original_cost'] = transaction.pop('originalCost')
            transaction['transaction_amount'] = transaction.pop('transactionAmount')
            transaction['billing_id'] = transaction.pop('billingId')
            transaction['service_id'] = transaction.pop('serviceId')

        await TransactionDao.add_transactions_list(transactions_list)
