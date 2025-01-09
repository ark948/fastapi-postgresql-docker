from sqlmodel import select
from fastapi import APIRouter, Depends
from backend.database.provider import get_async_session
from backend.database.models import User
from sqlalchemy.ext.asyncio.session import AsyncSession




router = APIRouter(
    prefix='/user'
)


from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    email: str
    password: str

from datetime import datetime

class ShowUser(BaseModel):
    id: int
    username: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime



@router.post('/', response_model=str, status_code=201)
async def create_user(data: CreateUser, db = Depends(get_async_session)):
    user_data_dict = data.model_dump()
    user_obj = User(**user_data_dict)
    db.add(user_obj)
    await db.commit()
    return "ok"



@router.get('/{item_id}', response_model=ShowUser, status_code=200)
async def get_user(item_id: int, db: AsyncSession = Depends(get_async_session)):
    user_obj = await db.get(User, item_id)
    if user_obj:
        print("\n", user_obj, "\n")
        return user_obj
    return None



@router.get('/v2/{item_id}', response_model=ShowUser, status_code=200)
async def get_user(item_id: int, db: AsyncSession = Depends(get_async_session)):
    user_obj = await db.scalar(select(User).where(User.id==item_id))
    if user_obj:
        print("\n", user_obj, "\n")
        return user_obj
    return None