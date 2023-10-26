from db import getThreadsInCategory , get_all_categories


def printAllThreads():
    categories=get_all_categories()
    for i in categories:
        threads = getThreadsInCategory(i)  # Replace with the category name you want to retrieve
        if threads:
            for thread in threads:
                print(f"Thread ID: {thread[0]}, Title: {thread[1]}, Content: {thread[2]}, Created At: {thread[3]}, Author: {thread[4]}")
        else:
            print("No threads found in the specified category.")



if __name__ == "__main__":
    printAllThreads()