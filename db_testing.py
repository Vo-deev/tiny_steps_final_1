from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from io import UnsupportedOperation
from operator import itemgetter
import os.path
import random
import json
from data import db_content


app = Flask(__name__)
app.secret_key = "randomstring"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# 1. Создайте модель "Преподаватель"
# – Установите и подключите SQLAlchemy.
# – Опишите модель для преподавателя.
# – Проверьте, что первичный ключ, типы и констрейнты в порядке.
# – upd: сохраните расписание в виде простой json-строки, при выводе превращайте строку в словарь.

@app.route('/profiles/<teacher_id>/')
class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    about = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.String, nullable=False)
    free = db.Column(db.Boolean)    # как правильно подтянуть?


user = Teacher()    # подтянуть данные из data.py
db.session.add(user)
db.session.commit()


# 2. Создайте модель "Бронирование"
# – Опишите модель Бронирование.
# – Свяжите модель отношениями с Преподавателем (one to many).
# – Проверьте, что первичный ключ, типы и констрейнты в порядке.

class Booking(db.Model):

    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    day = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)