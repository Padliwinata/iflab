from bson import json_util
import json
from db import db

def get_aslab():
    cursor = db.Aslab.find()
    json_string = json_util.dumps(cursor)
    data_dict = json.loads(json_string)
    return data_dict
