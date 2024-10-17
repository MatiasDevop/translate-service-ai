# database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import asynccontextmanager
#from my_secrets import DATABASE_URL

from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
print(f"DATABASE_URL---------: {SQLALCHEMY_DATABASE_URL}")  # Add this line to check

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)