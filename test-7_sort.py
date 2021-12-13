from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']


###sort input documents - ascending
test1 = db.menus.aggregate([{"$sort": {"name": 1}}])
print("####test-1####\n", list(test1))

###sort input documents - descending
test2 = db.menus.aggregate([{"$sort": {"price": -1}}])
print("####test-2####\n", list(test2))

###sort input documents - multiple fields
test3 = db.persons.aggregate([{"$sort": {"age": -1, "gender": 1}}])
print("####test-3####\n", list(test3))

###sort input documents - multiple stage
test4 = db.persons.aggregate([
    #stage-1
    {"$group": {"_id": "$favoriteFruit"}},
    #stage-2
    {"$sort": {"_id": 1}}
])
print("####test-4####\n", list(test4))

###sort input documents - multiple stage
test5 = db.persons.aggregate([
    #stage-1
    {"$group": {"_id": "$age"}},
    #stage-2
    {"$sort": {"_id": -1}}
])
print("####test-5####\n", list(test5))

###sort input documents - multiple stage
test6 = db.persons.aggregate([
    #stage-1
    {"$match": {"eyeColor" : {"$ne": "blue"}}},
    #stage-2
    {"$group": {"_id": {"eyeColor": "$eyeColor", "fruit": "$favoriteFruit"}}},
    #stage-3
    {"$sort": {"_id.eyeColor": 1, "_id.fruit": -1}}
])
print("####test-6####\n", list(test6))