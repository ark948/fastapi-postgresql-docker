from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import create_engine, text


from source.config import Config


async_engine = AsyncEngine(
    create_engine(url=Config.DB_URL)
)


async def init_db():
    async with async_engine.begin() as conn:
        statement = text("SELECT 'DATABASE CONNECTED';")
        result = await conn.execute(statement)
        print(result.all())