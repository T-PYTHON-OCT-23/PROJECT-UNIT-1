from db import getThreadsInCategory, get_all_categories, addCategory
from user import User
from post import Thread, Comment
from art import tprint
from colorama import Back
import hashlib
import re

# lambda for password validation

password_is_valid = lambda password: len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password)

# Lambda for email validation
email_valid = lambda email: len(email) <= 50 and bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

# Lambda for username validation (assuming usernames should be between 3 and 20 characters)
username_valid = lambda username: 3 <= len(username) <= 20 and bool(re.match(r'^[a-zA-Z0-9_]+$', username))

def allCategories():
    for category in get_all_categories():
        print(category)

def printAllThreads(category_name):
    threads = getThreadsInCategory(category_name)
    if threads:
        for thread in threads:
            print(f"Thread ID: {thread[0]}, Title: {thread[1]}, Content: {thread[2]}, Created At: {thread[3]}, Author: {thread[4]}")
    else:
        print("No threads found in the specified category.")

def registerUser():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        temp=password
        password = hashlib.sha256(password.encode()).hexdigest()[:50]
        email = input("Enter your email: ")
        if password_is_valid(temp):
            if email_valid(email):
                user = User(username, password, email)
                print(Back.GREEN + f"Created a new user with user ID {user.getUserId()}")
                break  # Exit the loop when registration is successful
            else:
                print(Back.RED + "Invalid email address. Please try again.")

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        password = hashlib.sha256(password.encode()).hexdigest()[:50]
        user = User.login(username, password)
        newUser = User(user[2], user[2], user[3])
        newUser.setId(user[0])
        if user:
            print(Back.GREEN + f"Logged in as user ID {newUser.getUserId()}")
            return user
        else:
            print(Back.RED + "Invalid username or password. Please try again.")

def addThread(user):
    content = input("Enter the content of the thread: ")
    title = input("Enter the title of the thread: ")
    Category= input("Enter the category of the thread: ")
    thread = Thread(title, content,Category, user)
    print(Back.GREEN + f"Created a new thread with thread ID {thread.thread_id}")
    
def addComment(user):
    content = input("Enter the content of the comment: ")
    thread_id = input("Enter the ID of the thread: ")
    comment = Comment(thread_id, content, user)
    print(Back.GREEN + f"Created a new comment with comment ID {comment.comment_id}")

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
            try:
                if user:
                    addThread(user)
                else:
                    print(Back.RED + "Please log in first.")
            except:
                print(Back.RED + "Please log in first.")
        elif choice == "6":
            try:
                if user:
                    addComment(user)
                else:
                    print(Back.RED + "Please log in first.")
            except:
                print(Back.RED + "Please log in first.")
        elif choice == "7":
            try:
                if user:
                    input_ = input("Enter the name of the category: ")
                    addCategory(input_)
                else:
                    print(Back.RED + "Please log in first.")
            except:
                print(Back.RED + "Please log in first.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print(Back.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
