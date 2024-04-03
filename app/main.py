from uuid import UUID, uuid4
from fastapi import FastAPI, Depends, Path
from sqlalchemy.orm import Session
from app import get_db, Student, StudentUpdate, StudentCreate

app = FastAPI()


@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    list_students = db.query(Student).all()
    return list_students


@app.put("/students/{student_id}")
def update_student_by_id(
    student_update: StudentUpdate,
    student_id: UUID = Path(..., description="The UUID of the student"),
    db: Session = Depends(get_db),
):
    student = (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .update({"name": student_update.name, "age": student_update.age})
    )
    if student:
        db.commit()
    return {"message": f"Student with student_id {student_id} updated successfully"}


@app.post("/students")
def add_student(student_create: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(
        student_id=uuid4(), name=student_create.name, age=student_create.age
    )
    db.add(new_student)
    db.commit()
    return {"message": "New student added successfully"}


@app.delete("/students/{student_id}")
def delete_student_by_id(student_id: UUID, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return {"message": f"Student with student_id {student_id} deleted successfully"}
