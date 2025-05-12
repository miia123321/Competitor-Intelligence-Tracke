from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Competitor(Base):
    __tablename__ = 'competitors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    website = Column(String, nullable=False)
    linkedin = Column(String)

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    competitor_id = Column(Integer)
    type = Column(String)
    headline = Column(String)
    url = Column(String)
    summary = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
