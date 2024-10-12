from sqlalchemy import Column, Integer,Text, String, DateTime, ForeignKey, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class TranslationTask(Base):
    __tablename__ = "translation_tasks"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    languages = Column(JSON, nullable=False)
    status = Column(String, default="in progress")

    translation = Column(JSON, default={})
