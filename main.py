from db import getThreadsInCategory , get_all_categories

def allCategories():
    for i in get_all_categories():
            print(i)

def printAllThreads(i):
        threads = getThreadsInCategory(i)  # Replace with the category name you want to retrieve
        if threads:
            for thread in threads:
                print(f"Thread ID: {thread[0]}, Title: {thread[1]}, Content: {thread[2]}, Created At: {thread[3]}, Author: {thread[4]}")
        else:
            print("No threads found in the specified category.")



if __name__ == "__main__":
    allCategories()
    printAllThreads(input("Enter The name of what category you want to see its threads:"))
    
