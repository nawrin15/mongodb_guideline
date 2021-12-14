from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']

## show selected field
test1 = db.menus.aggregate([{"$project": {"name": 1}}])
print("####test-1####\n", list(test1))


test2 = db.persons.aggregate([
    ##stage-1
    {"$project": {"_id":0, "name": 1, "isActive": 1, "gender": 1}}
])
print("####test-2####\n", list(test2))

test3 = db.persons.aggregate([
    ##stage-1
    {"$project": {"name": 0, "isActive": 0, "gender": 0}}
])
print("####test-3####\n", list(test3))

test4 = db.persons.aggregate([
    ##stage-1
    {"$project": {
        "_id": 0,
        "name": 1, 
        "info": {
            "eyes" : "$eyeColor",
            "fruit": "$favoriteFruit",
            "country": "$company.location.country"
        }
    }}
])
print("####test-4####\n", list(test4))