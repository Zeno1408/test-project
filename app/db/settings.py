from pydantic_settings import BaseSettings
from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Settings(BaseSettings):
    APP_NAME: str = "Student Management System"

    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    class Config:
        extra = "ignore"
        env_file = ".env"

    def get_sql_engine(self):
        engine = create_engine(
            f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:5432/{self.POSTGRES_DB}"
        )
        return engine

    def get_session(self):
        Session = sessionmaker(bind=self.get_sql_engine())
        session = Session()
        return session


@lru_cache
def get_settings():
    return Settings()
