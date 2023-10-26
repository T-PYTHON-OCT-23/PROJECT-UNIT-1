from db import getThreadsInCategory , get_all_categories
from user import User , Thread , Comment
from art import tprint
from colorama import Back
import hashlib 

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


def cliView():
    allCategories()
    printAllThreads(input("Enter The name of what category you want to see its threads:"))

def registerUser():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    password = hashlib.sha256(password.encode()).hexdigest()
    email = input("Enter your email: ")
    user = User(username, password, email)
    print(Back.green,f"Created a new user with user ID {user.userId}")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    password = hashlib.sha256(password.encode()).hexdigest()
    user = User.login(username, password)
    if user:
        print(Back.green,f"Logged in as user ID {user.userId}")
        return user

def addThread():
    login = login()
    content = input("Enter the content of the thread: ")
    title = input("Enter the title of the thread: ")
    thread = Thread(title, content, login.user)
    print(Back.green,f"Created a new thread with thread ID {thread.thread_id}")

def addComment():
    login = login()
    content = input("Enter the content of the comment: ")
    thread_id = input("Enter the ID of the thread: ")
    comment = Comment(thread_id, content, login.user)
    print(Back.green,f"Created a new comment with comment ID {comment.comment_id}")


def main():
    tprint("TECH", font='block')
    tprint("FORUM", font='block')

    while True:
        print("\nMenu:")
        print("1. View Categories")
        print("2. View Threads in a Category")
        print("3. Register")
        print("4. Login")
        print("5. Add Thread")
        print("6. Add Comment")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            allCategories()
        elif choice == "2":
            category_name = input("Enter the name of the category: ")
            printAllThreads(category_name)
        elif choice == "3":
            registerUser()
        elif choice == "4":
            user = login()
        elif choice == "5":
            if user:
                addThread(user)
            else:
                print(Back.red, "Please log in first.")
        elif choice == "6":
            if user:
                addComment(user)
            else:
                print(Back.red, "Please log in first.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
    
    