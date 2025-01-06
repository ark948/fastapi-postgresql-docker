from redis import asyncio as async_redis
from source.configs.settings import Config



async def get_redis():
    async with async_redis.Redis.from_url(Config.REDIS_URL) as client:
        yield client