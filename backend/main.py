from typing import Annotated
from fastapi import FastAPI, Depends, Body
from contextlib import asynccontextmanager
from backend.database.provider import init_db, get_async_session
from backend.cache.redis import get_redis
from sqlalchemy import text
from backend.config import settings



@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("---> [SERVER STARTED] <---")
    yield
    print("---> [SERVER SHUTDOWN] <---")




app = FastAPI(
    lifespan=lifespan
)


from backend.user import router as user_router
app.include_router(user_router)



@app.get('')
@app.get('/')
def root():
    return "async databas inside docker"



@app.get('/test')
def test():
    return {"message": "test successful"}



@app.get('/read-env')
def read_env():
    return settings.SECRET_KEY



@app.get('/test-db')
async def test_db_connection(db = Depends(get_async_session)):
    try:
        stmt = text("SELECT 'Hello From DB;'")
        result = await db.execute(stmt)
        result = result.all()
        print("\n\n", result, "\n\n")
        return "OK"
    except Exception as error:
        return "NOT OK"



@app.post('/test-redis')
async def test_redis_post(
        name: Annotated[str, Body(embed=True)], 
        value: Annotated[str, Body(embed=True)], 
        redis_client = Depends(get_redis)
    ):
    try:
        await redis_client.set(name=name, value=value, ex=3600)
        return "OK"
    except Exception as error:
        return "ERROR"
    


@app.get('/test-redis/{name}')
async def test_redis_get(name: str, redis_client = Depends(get_redis)):
    result = await redis_client.get(name)
    return result
    