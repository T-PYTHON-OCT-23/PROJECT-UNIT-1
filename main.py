from sign import *
from workout import * 
from calories import *  
from stringcolor import * 
from colorama import Fore, Back, Style
from art import * 
  

tprint("Welcome To Gym App" )

# overview 
print(Style.RESET_ALL)
print(cs("""The gym app will help you in your fitness journey.
The app provides a BMI calculator to check your health status as well as calories calculater and provides a workout based on user choice. \n""" , "blue"))
print(Style.RESET_ALL)


#sign in or sign up
phone_number= input("\n Enter your phone number: \n" )
name = input("Enter your name: \n")

try:
    user_check  = check_user( phone_number , name)
    print(user_check)
except Exception as e:
        print(cs(e ,"red"))
        phone_number= input("\n Enter your phone number: \n")
        name = input("Enter your name: \n")
        user_check  = check_user( phone_number , name)


print("\nPlease we would like to provide the information \n")

#take information from user
height = float(input ("Please enter your height: 'cm' \n"))
weight = float(input ("\nPlease enter your weight: 'kg' \n"))
age =float(input ("\nEnter your age: \n"))
gender = input("\nEnter your gender: F/M \n")
activity_level = input("\nEnter your level of activety:\n1. Sedentary (little or no exercise)\n2. Lightly active (light exercise/sports 1-3 days​/week)\n3. Moderately active (moderate exercise/sports 3-5 days/week)\n4. Very active (hard exercise/sports 6-7 days a week) \n5. Extra active (very hard exercise/sports & physical job or 2x training)\n")


#calculate bmi 
bmi = lambda  height ,weight : round(weight/((height/100)**2) ,2)     
var_bmi:float = bmi(height , weight)
user1 = Info(height , weight, age , gender , activity_level , bmi)

#show services
service_list = ["1. Personal information" , "2. BMI Calculater" ,
                "3. Calories Calculater" , "4. Choose workout" , "5. Exit"]
print()
#check services
while True: 
    service_input = input(cs(f"The services: \n{service_list }\n", "blue"))

#show user information 
    if service_input == "1": 
        per_info = sign_up.get(phone_number , name)
        print(cs(f"You registered with {per_info}\nBMI: {user1.Bmi_calculater(var_bmi)}\nCalories: {user1.calculate_daily_calories()}\n ", "blue"))

#check bmi 
    elif service_input == "2":
        print(user1.Bmi_calculater(var_bmi))

#calculate daily calories based on activity
    elif service_input == "3":
        print(user1.calculate_daily_calories())

#show workout based on user input
    elif service_input == "4":
        type_workout = input("Select your day push or pull or lower or abs:  \n")
        show_workout(type_workout)
        #print(list_workout)

#user must select a service or exit         
    elif service_input == "":
        print(cs("Please Chosse a service from the list", "red"))

    else:
         break
    

print(cs("Thank you for using Gym app", "yellow"))