from pymongo import MongoClient
import os
from dotenv import load_dotenv
import datetime
load_dotenv()

cluster = MongoClient(os.getenv('API_MONGO'))        #cluster name
db = cluster[os.getenv('MONGO_CLUSTER')]    #database name
    
def addToMongo(thread_id, title, content, category, author):
# Create a document with the data
    thread_data = {
        
        "thread_id": thread_id,
        "title": title,
        "content": content,
        "created_at": datetime.datetime.now(),
        "category": category.get_name(),
        "author": author
        
    }

    # Insert the document into a MongoDB collection
    collection = db[category.get_name()]
    collection.insert_one(thread_data)

def CreateCategories(category):
    db.create_collection(category)
    
def getThreads(category):
    collection = db[category]
    return collection.find({})


def getThreadById(category, thread_id):
    collection = db[category]
    return collection.find_one({"thread_id": int(thread_id)})


def removeThread(category, id):
    collection = db[category]
    collection.delete_one({"thread_id": id})

def getAllCategories():
    return db.list_collection_names()

def getThreadsInCategory(category):
    collection = db[category]
    return list(collection.find())


def addToCommentsMongo(thread_id, content, category, author):
# Create a document with the data
    Comment_data = {
        
        "thread_id": thread_id,
        "content": content,
        "created_at": datetime.datetime.now(),
        "category": category.get_name(),
        "author": author
        
    }

    # Insert the document into a MongoDB collection
    CommentToAdd="Comments/"+category.get_name()+"/"+thread_id
    collection = db[CommentToAdd]
    collection.insert_one(Comment_data)
    
    
def getComments(category, thread_id):
    CommentToAdd="Comments/"+category.get_name()+"/"+thread_id
    collection = db[CommentToAdd]
    return list(collection.find({}))

def removeCommentMongo(category, id, thread_id):
    CommentToAdd="Comments/"+category.get_name()+"/"+thread_id
    collection = db[CommentToAdd]
    collection.delete_one({"thread_id": id})