from flask import render_template, request
from src.config import app, db_content


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
