import uuid
from datetime import datetime
from pydantic.main import TupleGenerator
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy.types import Text
from sqlalchemy import ForeignKey
from typing import (
    Optional, List
)
from sqlmodel import (
    SQLModel, Field, Column, Relationship
)






class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True)
    username: str = Field(unique=True, nullable=False)
    email: str = Field(unique=True, nullable=False)
    password: str = Field(exclude=True)

    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f'<User {self.username}>'