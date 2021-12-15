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
    {"$project": {
        "name": 1,
        "eyeColorType": {"$type": "$eyeColor"},
        "ageType": {"$type": "$age"},
        "tagsType": {"$type": "$tags"},
        "companyType": {"$type": "$company"}

    }}
])
print("####test-1####\n", list(test1))