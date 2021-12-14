from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']

## show selected field
test1 = db.menus.aggregate([{"$limit": 2}])
print("####test-1####\n", list(test1))

test2 = db.persons.aggregate([
    {"$limit": 100},
    {"$match": {"age": {"$gt": 25}}},
    {"$group": {"_id": "$company.location.country"}}
])
print("####test-2####\n", list(test2))