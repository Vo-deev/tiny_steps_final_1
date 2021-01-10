from flask import render_template, request
import json
import os
from src.config import app, db_content


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
