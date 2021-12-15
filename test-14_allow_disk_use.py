from pymongo import MongoClient
client = MongoClient('mongodb://{}:{}@{}:{}/?authSource=admin'.format(
    'testuser',
    '123456',
    '0.0.0.0',
    '27017',
))
db = client['test_db']

#allow mongodb use Disk rather than ram incase of large datasets
test1 = db.persons.aggregate([], {"allowDiskUse": True})