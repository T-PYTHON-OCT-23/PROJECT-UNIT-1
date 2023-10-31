from modules import is_valid_email, is_valid_name,is_valid_password,get_valid_input,is_email_and_password_valid
import json
from payment import Payment
users = []
history_trips = []
email_user = "None"
# password_user = "None"
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
print(trips_duration[0])
print("Welcome to The Cycle Bark")
print(''' Note: your data is belong to you we insure you data privacy and we will not share it with other 3rd party''')
print(''' guid-lines :
      1) If you are new start with us.
      2) If you have an account. ''')
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
        print("For login email and password are requierd")
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
                email_user = user_email_input
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
                        "is_payed":"Not payed it yet"
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
                        "is_payed":"Not payed it yet"
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
                        "cost":trips_duration[0]['Aldryiah']['noura']['cost'],
                        "is_payed":"Not payed it yet"
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
                        "cost":trips_duration[0]['Aldryiah']['kuf']['cost'],
                        "is-payed":"Not payed it yet"
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
            user_trips_history = []
            if not email_user:
                print("pleaase login first")
            for u in history_trips:
                if email_user in u:
                    user_trips_history.append(u)
            print(''' 
        1) If you want to list all your trip.
        2) If you want to calculate all you bills and pay it. 
        3) If you want to exit the application.  ''')
            choise = int(input("Enter the number you have choise it: "))
            if choise == 1:
                for n in user_trips_history:
                    print(f"Your last trips where: from {n[email_user]['from']} to {n[email_user]['to']} an it cost you {n[email_user]['cost']} and you {n[email_user]['is_payed']}")
            elif choise ==2:
                list_not_payed = []
                total_cost = 0
                for index, n in enumerate(user_trips_history):
                    if n[email_user]['is_payed'] == "Not payed it yet":
                        list_not_payed.append(index)

                for idx, n in enumerate(list_not_payed):
                    total_cost += user_trips_history[n][email_user]['cost']
                    print(f"{idx+1}- You didn't payed trips from {user_trips_history[n][email_user]['from']} and you should pay {user_trips_history[n][email_user]['cost']} for it. ")
                
                print(f"And your total cost is {total_cost}")
                pay_it = input("Enter 'y' to pay it or 'n' to exit the application: ")
                consumer = Payment(email_user,total_cost)
                if pay_it == "y":
                    if consumer.is_it_payed(total_cost):
                        print("Paid successfully! Thank you and visit us again <3")
                        for n in list_not_payed:
                            user_trips_history[n][email_user]['cost'] = 0
                            user_trips_history[n][email_user]['is_payed'] = "PAYED"

                        with open("history.json", "w", encoding="utf-8") as file:
                            content = json.dumps(history_trips, indent=4)
                            file.write(content)
                        break
                    else:
                        break
                if pay_it == "n":
                    break
            elif choise ==3:
                break
        elif user_input == 3:
            with open("users.json", "w", encoding="utf-8") as file:
                content = json.dumps(users, indent=4)
                file.write(content)
            trips = False