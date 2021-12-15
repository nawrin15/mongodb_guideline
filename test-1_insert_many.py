from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']
# data = db['menus'].insert_many([
#     {
#         "name" : "burger",
#         "price" : 150
#     },
#     {
#         "name" : "cake",
#         "price" : 120
#     },
#     {
#         "name" : "pizza",
#         "price" : 1500
#     },
#     {
#         "name" : "coke",
#         "price" : 20
#     }
# ])
data = db['menus'].insert_many([
    {
        "name" : "burger",
        "price" : 170
    }
])
print(data)
