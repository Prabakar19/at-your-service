import asyncio
import sys

import sqlalchemy as sa
from aiopg.sa import create_engine

from config.config_loader import config_map

metadata = sa.MetaData(schema='atyourservice')

customer_tbl = sa.Table('customer', metadata,
                        sa.Column('customer_id', sa.Integer, primary_key=True),
                        sa.Column('customer_name', sa.String),
                        sa.Column('first_name', sa.String),
                        sa.Column('last_name', sa.String),
                        sa.Column('email_id', sa.String),
                        sa.Column('phone_number', sa.String),
                        sa.Column('password', sa.String))


async def go():
    async with create_engine(user=config_map['postgres']['user'],
                             database=config_map['postgres']['database'],
                             host=config_map['postgres']['host'],
                             port=config_map['postgres']['port'],
                             password=config_map['postgres']['password']) as engine:

        async with engine.acquire() as conn:
            async for row in conn.execute(customer_tbl.select()):
                print(row.customer_id, row.customer_name)


if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

loop = asyncio.get_event_loop()
loop.run_until_complete(go())
