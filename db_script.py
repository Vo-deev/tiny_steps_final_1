from src.data import *  # teachers, goals
from src.models import Teacher
from src.config import db
import json


# with open("db.json", "w") as f_obj:
#     content = dict()
#
#     content.update({"goals": goals})
#     content.update({"days": days})
#     content.update({"teachers": teachers[:]})
#
#     f_obj.write(json.dumps(content))

with open("db.json", "r") as f_obj:
    content = json.loads(f_obj.read())["teachers"]
    for teacher in content:
        formed_teacher = Teacher(
            name=teacher["name"],
            description=teacher["about"],
            picture=teacher["picture"],
            rating=teacher["rating"],
            price=teacher["price"],
            goals=",".join(teacher["goals"]),
            free=json.dumps(teacher["free"])
        )
        db.session.add(formed_teacher)
        db.session.commit()
