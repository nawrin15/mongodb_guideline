from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']


###group data by matching qurey - get matching object then grouping
test1 = db.persons.aggregate([
    ##stage-1
    {"$match": {"favoriteFruit": "banana"}},
    ##stage-2
    {"$group": { "_id": {"age": "$age", "eyeColor": "$eyeColor"}}}  
])
print("####test-1####\n", list(test1))

###group data by matching qurey - first grouping then get matching object

## didin't et any data because stage-1 data don't have favoriteFruit in document
test2 = db.persons.aggregate([
    ##stage-1
    {"$group": { "_id": {"age": "$age", "eyeColor": "$eyeColor"}}},
    ##stage-2
    {"$match": {"favoriteFruit": "banana"}},  
])
print("####test-2####\n", list(test2))


###group data by matching qurey - first grouping then get matching object

test3 = db.persons.aggregate([
    ##stage-1
    {"$group": { "_id": {"age": "$age", "eyeColor": "$eyeColor"}}},
    ##stage-2
    {"$match": {"_id.eyeColor": "blue"}},  
])
print("####test-3####\n", list(test3))


test4 = db.persons.aggregate([
    ##stage-1
    {"$group": { "_id": {"age": "$age", "eyeColor": "$eyeColor"}}},
    ##stage-2
    {"$match": {"_id.age": {"$gt": 38}}},  
])
print("####test-5####\n", list(test4))