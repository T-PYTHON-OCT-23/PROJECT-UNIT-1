


users = {}

print("Welcome to The Cycle Bark")
print(''' Note: your data is belong to you we insure you data privacy and we will not share it with other 3rd party''')
print(''' guid-lines :
      1) If you are new here Enter 1 to start with us
      2) If you have an account Enter 2 ''')
trips = True
while trips:
    try:
        user_input = int(input("please enter number here: "))
        if user_input < 0:
            print("Enter only positive number")
            input()
    except ValueError as e :
        print("Enter only a valid number")
        input()
    
    if user_input == 1:
        print(''' These feilds are requierd about personal information.
    1) User name
    2) Email
    3) Password''')
    
        user_name = input("Your name: ")
        if user_email == int:
            raise ValueError("the name should not start with number")
        user_email = input("Email: ")
        user_pass = input("Password: ")
    elif user_input == 2:
        pass
