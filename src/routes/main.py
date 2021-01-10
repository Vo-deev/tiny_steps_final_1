from flask import render_template, abort, request
from operator import itemgetter
import random
from src.config import app, db_content
from src.models import Teacher
import json


@app.route('/')
def main():  # all_teachers назвать, random.shuffle(db_content["teachers"][:6])
    teachers_info = Teacher.query.all()
    random.shuffle(teachers_info)
    return render_template('index.html', teachers_info=teachers_info[:6])


@app.route('/all/', methods=["GET", "POST"])
def all_teachers():  # ошибка Not Found, all.html в шаблоне
    teachers = Teacher.query.all()
    if request.method == "POST":
        choice = request.form.getlist("choice")[0]
        sort_teachers = {
            "best": Teacher.query.order_by(Teacher.rating.desc()).all(),
            "exp": Teacher.query.order_by(Teacher.price.desc()).all(),
            "chp": Teacher.query.order_by(Teacher.price.asc()).all()
        }
        return render_template("all.html", teachers=sort_teachers[choice])
    return render_template('all.html', teachers=teachers)


@app.route('/goals/<exact_goal>/')
def goals_(exact_goal):
    filtered_teachers = Teacher.query.filter(Teacher.goals.contains(exact_goal)).order_by(Teacher.rating.desc()).all()
    return render_template(
        'goal.html',
        teacher_info=filtered_teachers,
        goals=db_content["goals"],
        current_goal=exact_goal)


@app.route('/profiles/<teacher_id>/')
def profiles(teacher_id):
    teacher_info = Teacher.query.filter(Teacher.id == teacher_id).first()
    if teacher_info is not None:
        teacher_info.free = json.loads(teacher_info.free)
        return render_template(
            'profile.html',
            teacher_info=teacher_info,
            goals_description=db_content["goals"],
            days=db_content["days"]
        )
    else:
        abort(404)
