class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    def initialize():
        client = pymongo.MongoClient(Database.UTI)
        Database.DATABASE = client['fullstack']

    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    def find(collection, data):
        return Database.DATABASE[collection].find(data)

    def find_one(collection, data):
        return Database.DATABASE[collection]
