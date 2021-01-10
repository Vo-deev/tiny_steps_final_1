from sqlalchemy import Column, String, Integer
from src.config import db


class RequestModel(db.Model):
    id = Column(Integer, primary_key=True)
    goal = Column(String(16))
    time = Column(String(8))
    name = Column(String(32))
    phone = Column(String(32))
