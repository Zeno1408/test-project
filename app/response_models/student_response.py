from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class StudentResponse(BaseModel):
    student_id: UUID
    name: Optional[str]
    age: Optional[int]
