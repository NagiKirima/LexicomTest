import aioredis
from typing import AsyncGenerator
from settings import settings


async def get_redis_connection() -> AsyncGenerator[aioredis.Redis, None]:
    '''Get redis connnection with aioredis, return AsyncGenerator'''
    redis = await aioredis.from_url(settings.redis_url, password=settings.redis_password)
    try:
        yield redis
    finally:
        await redis.close()
