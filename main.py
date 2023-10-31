from modules import is_valid_email, is_valid_name,is_valid_password,get_valid_input,is_email_and_password_valid
import json

users = []
history_trips = []
email_user = "None"
password_user = "None"
trips_duration = []

try:
    with open("users.json", "r", encoding="utf-8") as file:
        content = file.read()
        users = json.loads(content)
    with open("history.json", "r", encoding="utf-8") as file:
        content = file.read()
        history_trips = json.loads(content)
    with open("tripDuration.json", "r", encoding="utf-8") as file:
        content = file.read()
        trips_duration = json.loads(content)
except Exception as e:
    print(e)
#with open("users.json","r+") as file:
#    users = json.loads(file)

print("Welcome to The Cycle Bark")
print(''' Note: your data is belong to you we insure you data privacy and we will not share it with other 3rd party''')
print(''' guid-lines :
      1) If you are new here Enter 1 to start with us.
      2) If you have an account Enter 2. ''')
trips = True
registration = True
login = True
while trips:
    if registration:
        try:
            user_input = int(input("please enter number here: "))
            if user_input < 0:
                print("Enter only positive number")
        except ValueError as e :
            print("Enter only a valid number")
    else:
        print("Login:")
        user_input = 2
    if user_input == 1:
        print(''' These feilds are requierd about personal information.
    1) User name
    2) Email
    3) Password''')
        user_name = get_valid_input("Full name: ", is_valid_name)
        user_email = get_valid_input("Email: ", is_valid_email)
        user_password = get_valid_input("Password: ", is_valid_password)
        print("Registration Successfully!")
        user_form = {
            user_email:{
                "user_name":user_name,
                "user_password":user_password
            }
        }
        users.append(user_form)
        with open("users.json", "w", encoding="utf-8") as file:
            content = json.dumps(users, indent=4)
            file.write(content)
        registration = False
    elif user_input == 2:
        left = 5
        while login:
            user_email_input = input("Email: ") 
            user_password_input = input("Password: ")
            #is_email_and_password_valid(user_email_input,user_password_input)
            if is_email_and_password_valid(user_email_input,user_password_input):
                break
            else:
                print(f"Try Again!, you have {left} left")
                left -= 1
                if left < 0:
                    login = False
        else:
            break

        print("Welcome to The Cycle Bark")
        print("To login insert your email and password below.")
        print(''' Menue: 
        1- To view the pathes you so you can pick a trips.
        2- To view history of your trips and payed it.
        3- To exit the application.''')
        try:
            user_input = int(input("Enter number here: "))
            if user_input < 0:
                print("Enter only positive number")
                input()
        except ValueError as e:
            print("Enter only a valid number")
            input()
        if user_input == 1:
            for idx ,n in enumerate(trips_duration):
                print(f''' Trips duration:
            {idx+1}- From Almasif to {n['almasif']['noura']['to']}, it will cost you {n['almasif']['noura']['cost']}
            {idx+2}- From Almasif to {n['almasif']['kfu']['to']}, it will cost you {n['almasif']['kfu']['cost']}
            {idx+3}- From Aldryiah to {n['Aldryiah']['noura']['to']}, it will cost you {n['Aldryiah']['noura']['cost']}
            {idx+4}- From Aldryiah to {n['Aldryiah']['kfu']['to']}, it will cost you {n['Aldryiah']['kfu']['cost']}
                      ''')
            try:
                user_choise_trip = int(input("Enter your trip number: "))
                if user_choise_trip < 0:
                    print("Enter only positive number")
                    input()
            except ValueError as e :
                print("Enter only a valid number")
                input()
            if user_choise_trip == 1:
                # travile animation if i want
                trip_format = {
                    email_user:{
                        "from":"almasif",
                        "to":"noura",
                        "cost":trips_duration[0]['almasif']['noura']['cost'],
                        "is_payed":"Not payed yet"
                    }
                }
                history_trips.append(trip_format)
                print("Enjoy your trip <3")
                with open("history.json", "w", encoding="utf-8") as file:
                    content = json.dumps(history_trips, indent=4)
                    file.write(content)
                trips = False
                registration = False
            elif user_choise_trip == 2:
                # travile animation if i want
                trip_format = {
                    email_user:{
                        "from":"almasif",
                        "to":"kfu",
                        "cost":trips_duration[0]['almasif']['kfu']['cost'],
                        "is_payed":"Not payed yet"
                    }
                }
                history_trips.append(trip_format)
                print("Enjoy your trip <3")
                with open("history.json", "w", encoding="utf-8") as file:
                    content = json.dumps(history_trips, indent=4)
                    file.write(content)
                trips = False
                registration = False
            elif user_choise_trip == 3:
                # travile animation if i want
                trip_format = {
                    email_user:{
                        "from":"Aldryiah",
                        "to":"noura",
                        "cost":trips_duration[1]['Aldryiah']['noura']['cost'],
                        "is_payed":"Not payed yet"
                    }
                }
                history_trips.append(trip_format)
                print("Enjoy your trip <3")
                with open("history.json", "w", encoding="utf-8") as file:
                    content = json.dumps(history_trips, indent=4)
                    file.write(content)
                trips = False
                registration = False
            elif user_choise_trip == 4:
                # travile animation if i want
                trip_format = {
                    email_user:{
                        "from":"Aldryiah",
                        "to":"kfu",
                        "cost":trips_duration[1]['Aldryiah']['kuf']['cost'],
                        "is-payed":"Not payed yet"
                    }
                }
                history_trips.append(trip_format)
                print("Enjoy your trip <3")
                with open("history.json", "w", encoding="utf-8") as file:
                    content = json.dumps(history_trips, indent=4)
                    file.write(content)
                trips = False
                registration = False
        elif user_input == 2:
            if not email_user:
                print("pleaase login first")
        elif user_input == 3:
            with open("users.json", "w", encoding="utf-8") as file:
                content = json.dumps(users, indent=4)
                file.write(content)
            trips = False