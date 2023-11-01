from modules import *
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

print("Welcome to The Cycle Bark")
trips = True
registration = True
login = True
start = True
count = 0
while trips:
    if registration:
        while start:
            try:
                if count <= 2:
                    print(''' Note: your data is belong to you we insure you data privacy and we will not share it with other 3rd party''')
                count +=1
                print_func()
                user_input = int(input("please enter number here: "))
                if user_input < 0:
                    print("Enter only positive number")
                    input("Press Enter to continue")
                elif user_input > 2:
                    print("Coution: Enter '1' or '2' ")
                    input("Press Enter to continue")
                elif user_input == 1 or user_input == 2:
                    start = False
            except ValueError as e :
                print("Enter only a valid number")
                input("Press Enter to continue")
    else:
        print("Note: For login email and password are requierd!")
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
        user_form = add_user_form(user_email,user_name,user_password)
        users.append(user_form)
        add_users(users)
        registration = False
    elif user_input == 2:
        left = 5
        while login:
            user_email_input = input("Email: ") 
            user_password_input = input("Password: ")
            if is_email_and_password_valid(user_email_input,user_password_input,users):
                email_user = user_email_input
                break
            else:
                print(f"Try Again!, you have {left} left")
                left -= 1
                if left < 0:
                    login = False
        else:
            break
        #start --- 
        l = True
        while l:
            print("Welcome to The Cycle Bark")
            print_function()
            try:
                user_input = int(input("Enter number here: "))
                if user_input < 0:
                    print("Enter only positive number")
                    input()
            except ValueError as e:
                print("Enter only a valid number")
                input()
            if user_input == 1:
                loops = True
                while loops:
                    print_trip_duration(trips_duration)
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
                        trip_format = add_trip1(email_user,trips_duration)
                        history_trips.append(trip_format)
                        print("Enjoy your trip <3")
                        history_write(history_trips)
                        exits = input("Enter 'exit' to exit or anything to continue: ")
                        if exits == "exit":
                            #trips = False
                            loops = False
                        
                    elif user_choise_trip == 2:
                        # travile animation if i want
                        trip_format = add_trip2(email_user,trips_duration)
                        history_trips.append(trip_format)
                        print("Enjoy your trip <3")
                        history_write(history_trips)
                        exits = input("Enter 'exit' to exit or anything to continue: ")
                        if exits == "exit":
                            #trips = False
                            loops = False

                    elif user_choise_trip == 3:
                        # travile animation if i want
                        trip_format = add_trip3(email_user,trips_duration)
                        history_trips.append(trip_format)
                        print("Enjoy your trip <3")
                        history_write(history_trips)
                        exits = input("Enter 'exit' to exit or anything to continue: ")
                        if exits == "exit":
                            #trips = False
                            loops = False

                    elif user_choise_trip == 4:
                        # travile animation if i want
                        trip_format = add_trip4(email_user,trips_duration)
                        history_trips.append(trip_format)
                        print("Enjoy your trip <3")
                        history_write(history_trips)
                        exits = input("Enter 'exit' to exit or anything to continue: ")
                        if exits == "exit":
                            #trips = False
                            loops = False

                    elif user_choise_trip == 404:
                        break
            elif user_input == 2:
                loop = True
                while loop:
                    user_trips_history = []
                    if not email_user:
                        print("pleaase login first")
                    for u in history_trips:
                        if email_user in u:
                            user_trips_history.append(u)
                    print_info()
                    choise = int(input("Enter the number you have choise it: "))
                    if choise == 1:
                        for n in user_trips_history:
                            print(f"Your last trips where: from {n[email_user]['from']} to {n[email_user]['to']} an it cost you {n[email_user]['cost']} and you {n[email_user]['is_payed']}")
                    elif choise ==2:
                        list_not_payed = []
                        total_cost = 0
                        list_not_payed = add_trip_not_payed_to_list(user_trips_history,email_user,list_not_payed)
                        total_cost = list_trip_not_payed(list_not_payed,user_trips_history,email_user,total_cost)
                        
                        print(f"And your total cost is {total_cost}")
                        pay_it = input("Enter 'y' to pay it or 'n' to exit the application: ")
                        consumer = Payment(email_user,total_cost)
                        if pay_it == "y":
                            if consumer.is_it_payed(total_cost):
                                print("Paid successfully! Thank you and visit us again <3")
                                for n in list_not_payed:
                                    user_trips_history[n][email_user]['cost'] = 0
                                    user_trips_history[n][email_user]['is_payed'] = "PAYED"
                                history_write(history_trips)
                            else:
                                break
                        if pay_it == "n":
                            break
                    elif choise ==3:
                        break
            elif user_input == 3:
                add_users(users)
                trips = False
                l = False