from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']


test1 = db.persons.aggregate([
    #
    {"$group": {
        "_id": "$age",
        "count": {"$sum": 1}
    }}
])
print("####test-1####\n", list(test1))

#unwind, group, sum
#count of each array element 
test2 = db.persons.aggregate([
    #stage-1
    {"$unwind": "$tags"},
    #stage-2
    {"$group": {
        "_id": "$tags",
        "count": {"$sum": 1}
    }}
])
print("####test2####\n", list(test2))

#count of each array element 
test3 = db.persons.aggregate([
    #stage-1
    {"$group": {
        "_id": "$eyeColor",
        "avgAge": {"$avg": "$age"}
    }}
])
print("####test3####\n", list(test3))

#count of each array element 
test4 = db.persons.aggregate([
    #stage-1
    {"$group": {
        "_id": "$company.location.country",
        "avgAge": {"$avg": "$age"}
    }}
])
print("####test4####\n", list(test4))