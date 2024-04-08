import random
from uuid import uuid4
from datetime import datetime
from faker import Faker
from db.settings import get_settings
from orm_models.models import Student, Standard, StudentExtra, Grade, Teacher

sql_session = get_settings().get_session()

fake = Faker()

grades_list = ["O", "A+", "A", "B+", "B", "C+", "C", "D", "E", "F"]
blood_group_list = ["O+", "O-", "AB+", "AB-", "A+", "A-", "B+", "B-"]
gender_list = ["Male", "Female", "Transgender"]

current_date = datetime.now().date()

for _ in range(10):
    student_id = uuid4()
    grade_id = uuid4()
    extra_id = uuid4()
    standard_id = uuid4()
    teacher_id = uuid4()

    dob = fake.date_of_birth(minimum_age=9, maximum_age=18)

    student = Student(
        id=student_id,
        class_id=standard_id,
        name=fake.name(),
        date_of_birth=dob,
        phone_number=fake.phone_number(),
        age=current_date.year - dob.year,
        gender=random.choice(gender_list),
        blood_group=random.choice(blood_group_list),
    )

    teacher = Teacher(id=teacher_id, name=fake.name())

    standard = Standard(
        id=standard_id, teacher_id=teacher_id, name=random.randint(1, 12)
    )

    grades = Grade(id=grade_id, student_id=student_id, grade=random.choice(grades_list))

    extra = StudentExtra(
        id=extra_id,
        student_id=student_id,
        father_name=fake.name_male(),
        mother_name=fake.name_female(),
        languages="Hindi, English, French",
        extra_curricular="Dancing, Sports, Quizzing, Coding",
    )

    sql_session.add_all([student, standard, extra, grades, teacher])

sql_session.commit()

print("All data added in the DB.")
