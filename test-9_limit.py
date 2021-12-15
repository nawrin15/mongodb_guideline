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
    #stage-1
    {"$limit": 100},
    #stage-2
    {"$match": {"age": {"$gt": 25}}},
    #stage-3
    {"$group": {"_id": "$company.location.country"}}
])
print("####test-2####\n", list(test2))

test3 = db.persons.aggregate([
    #stage-0
    {"$limit": 100},
    #stage-1
    {"$match": {"eyeColor" : {"$ne": "blue"}}},
    #stage-2
    {"$group": {"_id": {"eyeColor": "$eyeColor", "fruit": "$favoriteFruit"}}},
    #stage-3
    {"$sort": {"_id.eyeColor": 1, "_id.fruit": -1}}
])
print("####test-3####\n", list(test3))