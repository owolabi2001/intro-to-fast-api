from enum import Enum
from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    firstName: str
    lastName: str
    gender: Gender
    roles: list[Role]
    email: str | None = None