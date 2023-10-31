from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

cluster = MongoClient(os.getenv('API_MONGO'))        #cluster name
db = cluster[os.getenv('MONGO_CLUSTER')]    #database name
    
def addToMongo(thread_id, title, content, category, author):
# Create a document with the data
    thread_data = {
        
        "thread_id": thread_id,
        "title": title,
        "content": content,
        "category": category,
        "author": author
    }

    # Insert the document into a MongoDB collection
    collection = db[category]
    collection.insert_one(thread_data)

def CreateCategories(category):
    db.create_collection(category)
    
def getThreads(category):
    collection = db[category]
    return collection.find({})

def getThreadsById(category, id):
    collection = db[category]
    return collection.find({"thread_id": id})

def removeThread(category, id):
    collection = db[category]
    collection.delete_one({"thread_id": id})

def getAllCategories():
    return db.list_collection_names()