from flask import Flask, render_template, request
from io import UnsupportedOperation
from operator import itemgetter
import os.path
import random
import json
from data import db_content


app = Flask(__name__)
app.secret_key = "randomstring"


@app.route('/')
def main():  # all_teachers назвать, random.shuffle(db_content["teachers"][:6])
    teachers_info = db_content["teachers"][:]
    random.shuffle(teachers_info)
    return render_template('index.html', teachers_info=teachers_info[:6])


@app.route('/all/')
def all_teachers():  # ошибка Not Found, all.html в шаблоне
    return render_template('all.html', teachers=db_content["teachers"])


@app.route('/goals/<exact_goal>/')
def goals_(exact_goal):
    filtered_teachers = [teacher for teacher in db_content["teachers"] if exact_goal in teacher["goals"]]
    sorted_teachers = sorted(filtered_teachers, key=itemgetter("rating"))
    return render_template(
        'goal.html',
        teacher_info=sorted_teachers,
        goals=db_content["goals"],
        current_goal=exact_goal)


@app.route('/profiles/<teacher_id>/')
def profiles(teacher_id):
    teacher_info = [teacher for teacher in db_content["teachers"] if teacher["id"] == int(teacher_id)][0]
    return render_template(
        'profile.html',
        teacher_info=teacher_info,
        goals_description=db_content["goals"],
        days=db_content["days"]
    )


@app.route('/request')
def user_request():
    return render_template('request.html')


@app.route('/request_done', methods=["GET", "POST"])
def user_request_done():
    if request.method == "POST":
        data = {
            "goal": request.form.get("goal"),
            "time": request.form.get("time"),
            "name": request.form.get("name"),
            "phone": request.form.get("phone")
        }

        if not os.path.isfile("request.json"):
            os.mknod("request.json")

        with open("request.json", "r") as f_obj:
            try:
                content = json.loads(f_obj.read())
            except json.decoder.JSONDecodeError:
                content = {"requests": [data]}
            else:
                content["requests"].append(data)

        with open("request.json", "w") as f_obj:
            f_obj.write(json.dumps(content))

        return render_template('request_done.html', data=data, goals=db_content["goals"])


@app.route('/booking/<teacher_id>/<week_day>/<booking_time>/')
def booking_all(teacher_id, week_day, booking_time):
    booked_teacher = [teacher for teacher in db_content["teachers"] if teacher["id"] == int(teacher_id)][0]
    return render_template(
        "booking.html",
        teacher=booked_teacher,
        book_data=[week_day, booking_time],
        days=db_content["days"],
    )


@app.route('/booking_done', methods=["GET", "POST"])
def booking_done():
    if request.method == "POST":
        data = {
            "name": request.form.get("clientName"),
            "phone": request.form.get("clientPhone"),
            "day": request.form.get("clientWeekday"),
            "time": request.form.get("clientTime")
        }

        if not os.path.isfile("booking.json"):
            os.mknod("booking.json")

        with open("booking.json", "r") as f_obj:
            try:
                content = json.loads(f_obj.read())
            except json.decoder.JSONDecodeError:
                content = {"orders": [data]}
            else:
                content["orders"].append(data)

        with open("booking.json", "w") as f_obj:
            f_obj.write(json.dumps(content))

        return render_template('booking_done.html', data=data, days=db_content["days"])


if __name__ == '__main__':
    app.run()
