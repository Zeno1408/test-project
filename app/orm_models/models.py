from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID


class Base(DeclarativeBase):
    pass


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(UUID, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)

    standard = relationship("Standard", back_populates="teacher")


class Standard(Base):
    __tablename__ = "standard"
    id = Column(UUID, primary_key=True, nullable=False)
    teacher_id = Column(UUID, ForeignKey("teacher.id"), nullable=False)
    name = Column(Integer, nullable=False)

    student = relationship("Student", back_populates="standard")
    teacher = relationship("Teacher", back_populates="standard")


class Student(Base):
    __tablename__ = "students"

    id = Column(UUID, primary_key=True, nullable=False)
    class_id = Column(UUID, ForeignKey("standard.id"), nullable=False)
    name = Column(String(50), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    age = Column(Integer, nullable=False)
    phone_number = Column(String(50), nullable=False)
    gender = Column(String, nullable=False)
    blood_group = Column(String(50), nullable=False)

    standard = relationship("Standard", back_populates="student")
    grades = relationship("Grade", back_populates="student")
    extra = relationship("StudentExtra", back_populates="student")


class Grade(Base):
    __tablename__ = "grades"

    id = Column(UUID, primary_key=True, nullable=False)
    student_id = Column(UUID, ForeignKey("students.id"), nullable=False)
    grade = Column(String, nullable=False)

    student = relationship("Student", back_populates="grades")


class StudentExtra(Base):
    __tablename__ = "student_extra"

    id = Column(UUID, primary_key=True, nullable=False)
    student_id = Column(UUID, ForeignKey("students.id"), nullable=False)
    father_name = Column(String(50), nullable=False)
    mother_name = Column(String(50), nullable=False)
    languages = Column(String(100))
    extra_curricular = Column(String(200))

    student = relationship("Student", back_populates="extra")
