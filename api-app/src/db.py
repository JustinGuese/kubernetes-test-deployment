from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean, JSON, Float
from os import environ
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date


DATABASE_URL = "postgresql+psycopg2://" + environ["PSQL_URL"] # user:password@postgresserver/db

engine = create_engine(DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    connect_args={
        "keepalives": 1,
        "keepalives_idle": 30,
        "keepalives_interval": 10,
        "keepalives_count": 5,
    }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# cretaae db model sqlalchemy
class UserDB(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True)
    email = Column(String)
    password = Column(String)

# create pydantic model
class User(BaseModel):
    username: str
    email: str
    password: str

Base.metadata.create_all(bind=engine)
