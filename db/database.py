import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db").replace('postgres://', 'postgresql://')

connect_args = {"check_same_thread": False}
if SQLALCHEMY_DATABASE_URL and 'postgres' in SQLALCHEMY_DATABASE_URL:
    connect_args = {"sslmode": "require"}
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()