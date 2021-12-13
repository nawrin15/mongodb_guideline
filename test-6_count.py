from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']


###count input documents
test1 = db.menus.aggregate([{"$count": "allDocumentsCount"}])
print("####test-1####\n", list(test1))

test2 = db.persons.aggregate([{"$count": "allDocumentsCount"}])
print("####test-2####\n", list(test2))


test3 = db.persons.aggregate([
    ##stage-1
    {"$group": { "_id": "$eyeColor"}},
    ##stage-2
    {"$count": "eyeColor"}, #count of distinct values
])
print("####test-3####\n", list(test3))

test4 = db.persons.aggregate([
    ##stage-1
    {"$group": { "_id": "$age"}},
    ##stage-2
    {"$count": "age"}, #count of distinct values
])
print("####test-4####\n", list(test4))

test5 = db.persons.aggregate([
    ##stage-1
    {"$group": { "_id": {"eyeColor": "$eyeColor", "gender": "$gender"}}},
    ##stage-2
    {"$count": "eyeColorAndGender"}, #count of distinct values
])
print("####test-5####\n", list(test5))

test5 = db.persons.aggregate([
    {"$count": "total"}, #count of distinct values
])
print("####test-5####\n", list(test5))

test6 = db.persons.aggregate([
    ##stage-1
    {"$match": {"age": {"$lte": 25}}},
    ##stage-2
    {"$group": { "_id": {"age": "$age", "eyeColor": "$eyeColor"}}},
    #stage-3
    {"$count": "ageAndEyeColor"}, #count of distinct values
])
print("####test-6####\n", list(test6))

test6 = db.persons.aggregate([
    ##stage-1
    {"$match": {"eyeColor": "blue"}},
    ##stage-2
    {"$group": { "_id": {"age": "$age", "gender": "$gender"}}},
    #stage-3
    {"$count": "ageAndGender"}, #count of distinct values
])
print("####test-6####\n", list(test6))