from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']

test1 = db.persons.aggregate([
    #stage-1
    {"$group": {
        "_id": {
            "age": "$age",
            "eyeColor": "$eyeColor",
        }
    }},
    {"$out": "outCollection"}
    #stage-2
])
print("####test-1####\n", list(test1))