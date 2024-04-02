from uuid import UUID, uuid4
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import get_db, Student, StudentUpdate

app = FastAPI()


@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    list_students = db.query(Student).all()
    return list_students


@app.put("/students/{id}")
def update_student_by_id(
    student_id: UUID, student_update: StudentUpdate, db: Session = Depends(get_db)
):
    student = (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .update({"name": student_update.name, "age": student_update.age})
    )
    if student:
        db.commit()


@app.post("/student")
def add_student(name: str, age: int, db: Session = Depends(get_db)):
    new_student = Student(student_id=uuid4(), name=name, age=age)
    db.add(new_student)
    db.commit()


@app.delete("/students/{id}")
def delete_student_by_id(student_id: UUID, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
