import re
import json
import beepy
from colorama import Fore, Back, Style
users = []
with open("users.json", "r", encoding="utf-8") as file:
    content = file.read()
    users = json.loads(content)

def is_valid_email(email:str) -> any:
    pattern = r'^[\w\.-]+@[\w\.-]+(\.[\w]+)+$'
    for user in users:
        if email in user:
            return print("please enter a valid email")
    if re.match(pattern, email):
        return True
    return print("please enter a valid email")

def print_information() -> print:
     print(''' These feilds are requierd about personal information.
            1) User name
            2) Email
            3) Password''')
     
def is_valid_name(name:str) -> print:
    if all(char.isalpha() or char.isspace() for char in name):
        if len(name.strip()) > 0:
            return True
    return print("please enter a valid name")

def is_valid_password(password:int) -> bool:

    if len(password) < 8:
        return print("please enter at least 8 digits or character")
    
    if not re.search(r'[A-Z]', password) or \
       not re.search(r'[a-z]', password) or \
       not re.search(r'\d', password) or \
       not re.search(r'[^A-Za-z0-9]', password):
        return print("Note: requires at least one upper, one lower, one digit, and one special character")
    beepy.beep(sound='coin')
    return True

def add_trip2(email_user:str,trips_duration:dict) -> dict:
    trip_format = {
        email_user:{
            "from":"almasif",
            "to":"kfu",
            "cost":trips_duration[0]['almasif']['kfu']['cost'],
            "is_payed":"Not payed it yet"
        }}
    return trip_format

def add_trip3(email_user:str,trips_duration:dict) -> dict:
    trip_format = {
        email_user:{
            "from":"Aldryiah",
            "to":"noura",
            "cost":trips_duration[0]['Aldryiah']['noura']['cost'],
            "is_payed":"Not payed it yet"
            }
    }
    return trip_format

def history_write(history_trips) -> file:
    with open("history.json", "w", encoding="utf-8") as file:
        content = json.dumps(history_trips, indent=4)
        file.write(content)

def add_trip1(email_user:str,trips_duration:dict) -> dict:
    trip_format = {
         email_user:{
            "from":"almasif",
            "to":"noura",
            "cost":trips_duration[0]['almasif']['noura']['cost'],
            "is_payed":"Not payed it yet"
            }
    }
    
    return trip_format

def get_valid_input(prompt, validator_func) -> bool:
    tryes = True
    while tryes:
        user_input = input(prompt)
        if validator_func(user_input):
            return user_input

def add_trip4(email_user:str,trips_duration:dict) -> dict:
    trip_format = {
         email_user:{
            "from":"Aldryiah",
            "to":"kfu",
            "cost":trips_duration[0]['Aldryiah']['kfu']['cost'],
            "is_payed":"Not payed it yet"
            }
    }
    return trip_format
def is_email_and_password_valid(email:str,password,users:str) -> print:
    
    login_successful = False
    for user in users:
        if email in user and user[email]['user_password'] == password:
            login_successful = True
            return True

    if login_successful:
        print("Login successful")
    else:
        print("Invalid email or password")

def print_func() -> print:
    print(''' guid-lines :
            1) If you are new start with us.
            2) If you have an account. ''')
def add_user_form(user_email:str,user_name:str,user_password:str) -> dict:
    user_form = {
            user_email:{
            "user_name":user_name,
            "user_password":user_password
            }
        }
    
    return user_form
def print_color() -> print:
    print(Fore.GREEN,"Registration Successfully!")
    print(Style.RESET_ALL)

def print_note() -> print:
    print(Fore.RED,"Note: For login email and password are requierd!")
    print(Style.RESET_ALL)

def sound():
    beepy.beep(sound=1)

def outro():
    beepy.beep(sound=6)

def paid():
    beepy.beep(sound=4)

def trip_color() -> print:
    print(Fore.GREEN,"Enjoy your trip <3")
    print(Style.RESET_ALL)

def print_left(left) -> print:
    print(Fore.RED,f"Try Again!, you have {left} left")
    print(Style.RESET_ALL)

def print_function() -> print:
    print(''' Menue: 
            1- To view the pathes you so you can pick a trips.
            2- To view history of your trips and payed it.
            3- To exit the application.''')

def print_trip_duration(trips_duration:dict) -> print:
    for idx ,n in enumerate(trips_duration):
        print(f''' Trips duration:
            {idx+1}- From Almasif to {n['almasif']['noura']['to']}, it will cost you {n['almasif']['noura']['cost']}
            {idx+2}- From Almasif to {n['almasif']['kfu']['to']}, it will cost you {n['almasif']['kfu']['cost']}
            {idx+3}- From Aldryiah to {n['Aldryiah']['noura']['to']}, it will cost you {n['Aldryiah']['noura']['cost']}
            {idx+4}- From Aldryiah to {n['Aldryiah']['kfu']['to']}, it will cost you {n['Aldryiah']['kfu']['cost']}
                            ''')
    print("Enter '404' to exit the application.")

def print_info() -> print:
    print(''' 
            1) If you want to list all your trip.
            2) If you want to calculate all you bills and pay it. 
            3) If you want to 'Back'.  ''')

def add_users(users:dict) -> file:
    with open("users.json", "w", encoding="utf-8") as file:
        content = json.dumps(users, indent=4)
        file.write(content)

def add_trip_not_payed_to_list(user_trips_history:list,email_user:str,list_not_payed:list) -> list:
    for index, n in enumerate(user_trips_history):
        if n[email_user]['is_payed'] == "Not payed it yet":
            list_not_payed.append(index)
    
    return list_not_payed

def list_trip_not_payed(list_not_payed:list,user_trips_history:dict,email_user:str,total_cost:int) -> int:
    for idx, n in enumerate(list_not_payed):
        total_cost += user_trips_history[n][email_user]['cost']
        print(f"{idx+1}- You didn't payed trips from {user_trips_history[n][email_user]['from']} and you should pay {user_trips_history[n][email_user]['cost']} for it. ")
    return total_cost

def read_user() -> file:
    with open("users.json", "r", encoding="utf-8") as file:
        content = file.read()
        users = json.loads(content)
    return users

def read_history() -> file :
    with open("history.json", "r", encoding="utf-8") as file:
        content = file.read()
        history_trips = json.loads(content)
    return history_trips

def read_trip() -> file:
    with open("tripDuration.json", "r", encoding="utf-8") as file:
        content = file.read()
        trips_duration = json.loads(content)
        return trips_duration