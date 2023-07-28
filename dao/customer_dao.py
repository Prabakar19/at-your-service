from sqlalchemy import Column, String, select
import sqlalchemy as sa
from service.portgresql.postgres_provider import DbBase, PostgresProvider


class CustomerDao(DbBase):
    __tablename__ = 'customer'
    customer_id = Column(String, name='customer_id', primary_key=True)
    customer_name = Column(String, name='customer_name', primary_key=True)
    first_name = Column(String, name='first_name', primary_key=True)
    last_name = Column(String, name='last_name', primary_key=True)
    email_id = Column(String, name='email_id', primary_key=True)
    phone_number = Column(String, name='phone_number', primary_key=True)
    password = Column(String, name='password', primary_key=True)

    # address = relationship('Address')

    @classmethod
    async def add_customer(cls, customer):
        query = [sa.insert(CustomerDao).values(customer)]
        await PostgresProvider.execute(query)

    @classmethod
    async def get_customer_by_name(cls, customer_name: str):
        query = select(CustomerDao).where(cls.customer_name == customer_name)
        await PostgresProvider.execute(query)

    @classmethod
    async def get_customer_by_id(cls, customer_id: str):
        query = select(CustomerDao).where(cls.customer_id == customer_id)
        await PostgresProvider.execute(query)

    @classmethod
    async def update_customer(cls, customer):
        query = [sa.update(CustomerDao).where(cls.name == customer['name']).values(customer)]
        await PostgresProvider.execute(query)
