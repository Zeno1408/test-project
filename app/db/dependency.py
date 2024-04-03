from app.db.settings import get_settings

sql_session = get_settings().get_session()


# Dependency: Get a database session
def get_db():
    db = sql_session
    try:
        yield db
    finally:
        db.close()
