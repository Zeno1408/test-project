from uuid import UUID, uuid4
from fastapi import FastAPI, Depends, Path
from sqlalchemy.orm import Session
from app.orm_models.models import Grade, StudentExtra, Standard
from app import get_db, Student, StudentUpdate, StudentCreate, StudentResponse

app = FastAPI()


@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    list_students = db.query(Student).all()
    return list_students


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student_by_id(
    student_id: UUID = Path(..., description="The UUID of the student"),
    db: Session = Depends(get_db),
):
    student = db.query(Student).filter(Student.id == student_id).first()
    return student


@app.get("/grades/{student_id}")
def get_student_grade(
    student_id: UUID = Path(..., description="The UUID of the student"),
    db: Session = Depends(get_db),
):
    student_grade = db.query(Grade).filter(Grade.student_id == student_id).first()
    return student_grade


@app.get("/student_details")
def get_student_details(
    db: Session = Depends(get_db),
):
    all_student_details = db.query(StudentExtra).all()
    return all_student_details


@app.get("/standard")
def get_standard(
    db: Session = Depends(get_db),
):
    standard = db.query(Standard).all()
    return standard


@app.get("/student_details/{student_id}")
def get_student_grade(
    student_id: UUID = Path(..., description="The UUID of the student"),
    db: Session = Depends(get_db),
):
    student_details = (
        db.query(StudentExtra).filter(StudentExtra.student_id == student_id).first()
    )
    return student_details


@app.delete("/student_details/{student_id}")
def delete_student_grade(
    student_id: UUID = Path(..., description="The UUID of the student"),
    db: Session = Depends(get_db),
):
    student_details = (
        db.query(StudentExtra).filter(StudentExtra.student_id == student_id).first()
    )
    if student_details:
        db.delete(student_details)
        db.commit()
    return f"Student with student_id {student_id} deleted successfully."


@app.put("/students/{student_id}")
def update_student_by_id(
    student_update: StudentUpdate,
    student_id: UUID = Path(..., description="The UUID of the student"),
    db: Session = Depends(get_db),
):
    student = (
        db.query(Student)
        .filter(Student.id == student_id)
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
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return {"message": f"Student with student_id {student_id} deleted successfully"}
