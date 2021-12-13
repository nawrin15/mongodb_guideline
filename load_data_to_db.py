##DIDN't WORK


from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['persons']

from bson import json_util

import bson
with open('sample_data.bson', 'rb') as f:
    data = json_util.dumps(f.read())
    data1 = json_util.loads(data)
    db.persons.insert_many(data1)

