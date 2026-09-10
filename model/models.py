from sqlmodel import SQLModel, Field
from typing import Optional
import uuid

class User(SQLModel, table=True):
    
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        nullable=False,
        max_length=36
    )

    username: str = Field(unique=True)

    email: str = Field(unique=True)

    password: str



class LoginRequest(SQLModel):
    email: str
    password: str