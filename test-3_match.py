from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']

print(list(db.menus.find({ "name" : "burger"})))
### get the match data based on query 
test1 = db.menus.aggregate([
    ##stage-1
    {"$match": { "name" : "burger"}}
])
###same result as --> db.menus.find({ "name" : "burger"})
print("####test1####\n", list(test1))


test2 = db.menus.aggregate([
    ##stage-1
    {"$match": { "price" : {"$gte" : 170}}}
])
print("####test2####\n", list(test2))



test3 = db.persons.aggregate([
    ##stage-1
    {"$match": { "isActive" : True}}
])
print("####test3####\n", list(test3))



test4 = db.persons.aggregate([
    ##stage-1
    {"$match": { "tags" : {"$size":3}}}
])
print("####test4####\n", list(test4))


