from typing import Optional
from pydantic import BaseModel


class StudentUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]


class StudentCreate(BaseModel):
    name: Optional[str]
    age: Optional[int]
