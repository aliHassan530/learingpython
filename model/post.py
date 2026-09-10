# from pydantic import BaseModel
# class PostCreate(BaseModel):
#     content: str
from typing import Optional
from sqlmodel import SQLModel, Field


class Post(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    user_id: str = Field(
        foreign_key="user.id",
        nullable=False
    )

    content: str


class PostCreate(SQLModel):
    content: str