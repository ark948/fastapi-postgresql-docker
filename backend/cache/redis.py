from redis import asyncio as async_redis
from backend.config import settings



async def get_redis():
    async with async_redis.Redis.from_url(settings.REDIS_URL) as client:
        yield client