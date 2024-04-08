from db.settings import get_settings
from orm_models.models import Student, Standard, StudentExtra, Grade, Teacher


db = get_settings().get_session()

query = db.query(Standard.name, Standard.teacher_id, Teacher.id).join(
    Teacher, Standard.teacher_id == Teacher.id
)
print(list(query))
