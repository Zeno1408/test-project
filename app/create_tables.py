from db.settings import get_settings
from orm_models.models import Base

sql_engine = get_settings().get_sql_engine()

Base.metadata.create_all(bind=sql_engine)
