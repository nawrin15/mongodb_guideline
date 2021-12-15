from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']


test1 = db.persons.aggregate([
    {"$group": {"_id": "$tags"}}
])
print("####test-1####\n", list(test1))

test2 = db.persons.aggregate([
    {"$unwind": "$tags"}
])
print("####test-2####\n", list(test2))

test3 = db.persons.aggregate([
    {"$unwind": "$tags"},
    {"$project": {"name": 1, "index": 1, "tags": 1 }}
])
print("####test-3####\n", list(test3))

#most useful
test3 = db.persons.aggregate([
    #stage-1
    {"$unwind": "$tags"},
    #stage-2
    {"$group": {"_id": "$tags"}}
])
print("####test-3####\n", list(test3))