import asyncpg
from typing import AsyncGenerator
import time
from functools import wraps

from settings import settings


async def get_db_connection() -> AsyncGenerator[asyncpg.Connection, None]:
    '''Return AsyncGenerator with asyncpg connection, finally close connection'''
    connection = await asyncpg.connect(
        host=settings.db_host,
        port=settings.db_port,
        user=settings.db_user,
        password=settings.db_password,
        database=settings.db_name
    )
    try:
        yield connection
    finally:
        await connection.close()


async def db_init():
    '''Init database from init.sql file, init.sql create full_names and short_names table and truncate them'''
    
    with open("sql/init.sql", "r") as file:
        sql_script = file.read()

    async for connection in get_db_connection():
        await connection.execute(sql_script)


def time_wrapper(func):
    '''Decorator to measure function execution time'''
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        end = time.time()

        print(f"Execution time: {(end - start)} seconds")

        return result

    return wrapper


@time_wrapper
async def execute_query(query: str):
    '''Execute sql query'''
    async for connection in get_db_connection():
        await connection.execute(query)
