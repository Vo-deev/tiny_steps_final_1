from data import *  # teachers, goals
import json


with open("db.json", "w") as f_obj:
    content = dict()

    content.update({"goals": goals})
    content.update({"days": days})
    content.update({"teachers": teachers[:]})

    f_obj.write(json.dumps(content))
