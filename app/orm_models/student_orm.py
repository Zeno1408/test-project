from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    student_id = Column(UUID, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
