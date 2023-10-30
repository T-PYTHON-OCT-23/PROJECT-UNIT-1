from pymongo import MongoClient
import json
import os
cluster = MongoClient(os.getenv("API_MONGO"))        #cluster name
db = cluster["TECH_Fourms"]    #database name

class Mongo:
    def __init__(self, host, port, database):
        self.client = MongoClient(host, port)
        self.db = self.client[database]

    def addToMongo(self, thread_id, title, content, category, author):
        # Create a document with the data
        thread_data = {
            "thread_id": thread_id,
            "title": title,
            "content": content,
            "category": category,
            "author": author
        }

        # Insert the document into a MongoDB collection
        collection = self.db[category]
        collection.insert_one(thread_data)

    def getCategories(self, category):
         for i in category:
            db.create_collection(i)
            
    def getThreads(self, category):
        collection = self.db[category]
        return collection.find({})
    
    def getThredsById(self, category, id):
        collection = self.db[category]
        return collection.find({"thread_id": id})
    
    def removeThread(self, category, id):
        collection = self.db[category]
        collection.delete_one({"thread_id": id})