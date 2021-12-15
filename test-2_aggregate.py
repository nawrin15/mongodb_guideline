from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']
data = db['menus'].find({})


###get all the value
#way-1
data1 = db.menus.aggregate([])
print(list(data1))
#way-2
data2 = db['menus'].aggregate([])
print(list(data2))
#way-3
data3 = db['menus'].find({})
print(list(data3))
