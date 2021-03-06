import pymongo

__author__ = 'Dartaku'


class Database(object):
    URI = "mongodb://127.0.0.1:27017" #Universal Resource Identifier
    DATABASE = None

    @staticmethod
    def initialize() -> object:
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['test']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
       return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
       return Database.DATABASE[collection].find_one(query)

    # MongoDB Syntax
    # db.collectionname.find({}).pretty() - To find all the data in that collection name