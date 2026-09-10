from sqlmodel import SQLModel, Field
from typing import Optional
import uuid


class User(SQLModel, table=True):
    # id: Optional[int] = Field(default=None, primary_key=True)
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        nullable=False,
        max_length=36
    )
    username: str
    email: str
    password: str