from typing import Annotated
from fastapi import Depends
from redis import Redis
from redis import asyncio as async_redis
from source.config import Config


# jwt id
JTI_EXPIRY = 3600


# await redis_client.set(name=jti, value="", ex=JTI_EXPIRY)
# jti = await redis_client.get(jti)



async def get_redis():
    async with async_redis.Redis.from_url(Config.REDIS_URL) as client:
        yield client


getRedisDep = Annotated[Redis, Depends(get_redis)]