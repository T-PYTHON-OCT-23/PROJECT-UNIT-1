from modules import is_valid_email, is_valid_name,is_valid_password,get_valid_input


users = []

print("Welcome to The Cycle Bark")
print(''' Note: your data is belong to you we insure you data privacy and we will not share it with other 3rd party''')
print(''' guid-lines :
      1) If you are new here Enter 1 to start with us.
      2) If you have an account Enter 2. ''')
trips = True
registration = True
while trips:
    if registration:
        try:
            user_input = int(input("please enter number here: "))
            if user_input < 0:
                print("Enter only positive number")
                input()
        except ValueError as e :
            print("Enter only a valid number")
            input()
    else:
        user_input = 2
    if user_input == 1:
        print(''' These feilds are requierd about personal information.
    1) User name
    2) Email
    3) Password''')
        user_name = get_valid_input("Full namesw: ", is_valid_name)
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
        registration = False
    elif user_input == 2:
        pass
