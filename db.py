from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
# from dotenv.main import load_dotenv
import os

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:juancarlos23@localhost:5432/bookStore"

engine = create_engine( SQLALCHEMY_DATABASE_URL )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
  Base.metadata.create_all(bind=engine)
    
def get_db():
  db = SessionLocal()
  try:
    yield db
    db.commit()
  finally:
    db.close()
    
db_dependency = Annotated[ Session, Depends(get_db)]
