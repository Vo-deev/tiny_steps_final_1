from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
import json


app = Flask(__name__)
app.secret_key = "randomstring"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

try:
    with open("db.json", "r") as f_obj:
        db_content = json.loads(f_obj.read())
except json.decoder.JSONDecodeError as e:
    print(e)
