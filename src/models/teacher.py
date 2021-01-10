from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from src.config import db


class Teacher(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    description = Column(Text)
    picture = Column(String(64), unique=True)
    rating = Column(Integer)
    price = Column(Integer)
    goals = Column(String(128))
    free = Column(Text)
    orders = relationship('Order', back_populates='teacher')


class Order(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    phone = Column(String(32))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    teacher = relationship('Teacher', back_populates='orders')