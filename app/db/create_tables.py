from app.db.settings import get_settings
from app.orm_models.student_orm import Base

sql_engine = get_settings().get_sql_engine()
sql_session = get_settings().get_session()

Base.metadata.create_all(bind=sql_engine)
