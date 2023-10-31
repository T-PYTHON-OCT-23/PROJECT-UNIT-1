import re
import json

users = []
with open("users.json", "r", encoding="utf-8") as file:
    content = file.read()
    users = json.loads(content)

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+(\.[\w]+)+$'
    if re.match(pattern, email):
        return True
    return print("please enter a valid email")

def is_valid_name(name):
    if all(char.isalpha() or char.isspace() for char in name):
        if len(name.strip()) > 0:
            return True
    return print("please enter a valid name")

def is_valid_password(password):

    if len(password) < 8:
        return print("please enter at least 8 digits or character")
    
    if not re.search(r'[A-Z]', password) or \
       not re.search(r'[a-z]', password) or \
       not re.search(r'\d', password) or \
       not re.search(r'[^A-Za-z0-9]', password):
        return print("Note: requires at least one upper, one lower, one digit, and one special character")
    return True

def get_valid_input(prompt, validator_func):
    tryes = True
    while tryes:
        user_input = input(prompt)
        if validator_func(user_input):
            return user_input

def is_email_and_password_valid(email,password):
    
    login_successful = False
    for user in users:
        if email in user and user[email]['user_password'] == password:
            login_successful = True
            return True

    if login_successful:
        print("Login successful")
    else:
        print("Invalid email or password")
        
