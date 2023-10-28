import re

class cycle:
    pass

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
    # Check the minimum length requirement
    if len(password) < 8:
        return print("please enter at least 8 digits or character")

    # Check for complexity (requires at least one upper, one lower, one digit, and one special character)
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