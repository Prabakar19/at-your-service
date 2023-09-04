import datetime
from typing import List, Dict, Any

from dao.billing_dao import BillingDao
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

    async def get_all_cust_transaction(self, customer_id: str):
        billings = await BillingDao.get_billing_by_customer_id(customer_id)
        billing_ids = list(set([billing['billing_id'] for billing in billings]))
        transaction_list = await TransactionDao.get_transaction_by_billing_ids(billing_ids)
        for transaction in transaction_list:
            self.transform_transaction_for_ui(transaction)

        return transaction_list

    async def update_rating(self, transaction_id: str, rating: Dict[str, any]):
        txn = await TransactionDao.update_rating(transaction_id, rating['rating'])
        service_txns = await TransactionDao.get_transaction_by_service_id(txn['service_id'])
        total_rating = valid_count = 0
        for txn in service_txns:
            if txn['transaction_rating']:
                total_rating += txn['transaction_rating']
                valid_count += 1

        total_rating = total_rating/valid_count
        await ServiceDao.update_rating(txn['service_id'], total_rating)
        self.transform_transaction_for_ui(txn)
        return txn

    @staticmethod
    def transform_transaction_for_ui(transaction: Dict[str, Any]):
        transaction['transactionId'] = transaction.pop('transaction_id')
        transaction['serviceId'] = transaction.pop('service_id')
        transaction['billingId'] = transaction.pop('billing_id')
        transaction['transactionRating'] = transaction.pop('transaction_rating')
        transaction['transactionAmount'] = transaction.pop('transaction_amount')
        transaction['originalCost'] = transaction.pop('original_cost')
        transaction['date'] = transaction.pop('transaction_time')
