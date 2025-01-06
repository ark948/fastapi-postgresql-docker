from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import create_engine, text
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import AsyncGenerator
from sqlalchemy.orm import sessionmaker


from source.configs.settings import Config


async_engine = AsyncEngine(create_engine(url=Config.DB_URL))


async def init_db():
    async with async_engine.begin() as conn:
        statement = text("SELECT 'DATABASE CONNECTED';")
        result = await conn.execute(statement)
        print(result.all())


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    Session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

    async with Session() as session:
        try:
            yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()