from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']


###group data by name  
test1 = db.menus.aggregate([
    {"$group": { "_id": "$name"}}  ## get all distinct value of name field
])

print("####test-1####\n", list(test1))
## output - [{'_id': 'coke'}, {'_id': 'burger'}, {'_id': 'cake'}, {'_id': 'pizza'}]

###group data by eyecolor 
test2 = db.persons.aggregate([
    {"$group": { "_id": "$eyeColor"}}  ## get all distinct value of name field
])

print("####test-2####\n", list(test2))

###group data by age and gender 
test3 = db.persons.aggregate([
    {"$group": { "_id": {"age": "$age", "gender": "$gender"}}}  ## get all distinct value of name field
])

print("####test-3####\n", list(test3))

###group data by nested fields
test4 = db.persons.aggregate([
    {"$group": { "_id": "$company.location.country"}}  ## get all distinct value of name field
])

print("####test-4####\n", list(test4))

###group data by nested fields
test5 = db.persons.aggregate([
    {"$group": { "_id": {
        "fruit": "$favoriteFruit", 
        "Eye Color": "$eyeColor"
    }}
    }  ## get all distinct value of name field
])

print("####test-4####\n", list(test5))

##group data by name and sum the price 
test6 = db.menus.aggregate([
    {"$group": { "_id": "$name", "total": {"$sum": "$price"}}}
])
print("####test-6####\n", list(test6))
