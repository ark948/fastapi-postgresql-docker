from fastapi import FastAPI
from contextlib import asynccontextmanager
from source.database import init_db
from source.config import Config



@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield




app = FastAPI(
    lifespan=lifespan
)




@app.get('')
@app.get('/')
def root():
    return "async databas inside dockere"



@app.get('/test')
def test():
    return {"message": "test successful"}



@app.get('/read-env')
def read_env():
    return Config.SECRET_KEY