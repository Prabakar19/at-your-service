from contextlib import asynccontextmanager
from datetime import date, datetime
from typing import Any, List, Dict
from typing import ClassVar, Optional
from uuid import UUID

from aiopg.sa import create_engine, Engine
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

from config.config_loader import config_map

metadata = MetaData(schema='atyourservice')
DbBase = declarative_base(metadata=metadata)


class DbConnectionPool:
    _engine: ClassVar[Optional[Engine]] = None

    @asynccontextmanager
    async def get_connection(self):
        engine = await self._get_engine()
        async with engine.acquire() as conn:
            yield conn

    async def _get_engine(self):
        if self._engine is None:
            self._engine = await create_engine(
                user=config_map['postgres']['user'],
                database=config_map['postgres']['database'],
                host=config_map['postgres']['host'],
                port=config_map['postgres']['port'],
                password=config_map['postgres']['password'], echo=False)
        return self._engine


class PostgresProvider:
    pool: ClassVar[DbConnectionPool] = DbConnectionPool()

    @classmethod
    async def execute(cls, query):
        async with cls.pool.get_connection() as conn:
            return await conn.execute(query)

    @classmethod
    async def execute_transaction(cls, statement):
        async with cls.pool.get_connection() as conn:
            transaction = await conn.begin()
            try:
                for s in statement:
                    await conn.execute(s)
            except Exception as e:
                await transaction.rollback()
                print('DB error %s. rolling back Transaction' % e)
                raise ValueError('DB error %s. rolling back Transaction' % e)
            else:
                await transaction.commit()

    @classmethod
    async def get_list(cls, query) -> List[Dict[str, Any]]:
        async with cls.pool.get_connection() as conn:
            result = []
            async for row in await conn.execute(query):
                keys = row._result_proxy.keys
                values = []
                for val in row._row:
                    if type(val) in [str, date, UUID, datetime]:
                        val = str(val)
                    values.append(val)
                result.append(dict(zip(keys, values)))
            return result
