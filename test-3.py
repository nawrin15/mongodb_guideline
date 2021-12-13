from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']
data = db['menus'].find({})


###group data by name and sum the price 
data1 = db.menus.aggregate([
    {"$group": { "_id": "$name", "total": {"$sum": "$price"}}}
])
print(list(data1))
