from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

class Mongo:
    def __init__(self):
        self.cluster = MongoClient(os.getenv('API_MONGO'))        #cluster name
        self.db = self.cluster[os.getenv('MONGO_CLUSTER')]    #database name
    
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
        self.db.create_collection(i)
    
def getThreads(self, category):
    collection = self.db[category]
    return collection.find({})

def getThreadsById(self, category, id):
    collection = self.db[category]
    return collection.find({"thread_id": id})

def removeThread(self, category, id):
    collection = self.db[category]
    collection.delete_one({"thread_id": id})
    
techDB=Mongo()
