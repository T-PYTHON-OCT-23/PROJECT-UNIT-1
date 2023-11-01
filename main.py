from art import * 
from colorama import Fore, Back, Style
from costumers import *
from products import *


    

tprint("WELCOME IN OUR WEBSITE \n our resturant welcomes you  \n")


print(Fore.BLUE + " Register with us to reach you as quickly as possible ")


products_ = { 
	"checken_burger" : {
		"cheese" : True,
		"lettuce" : True,
		"mayonnaise":True,
		"meal" : True

	},
	"meet_burger" : {
		"cheese" : True,
		"lettuce" : True,
		"mayonnaise":True,
		"meal" : True

	}

}
#PRODUCTs__=[cheken_burger]


cosumers = {
        "phone_number" : " ",
        "name" : " ",
        "email" : " ",
        "adress" :{
            "city" : " ",
            "quarter": " ",
            "street":" "
        }

    }


product = Product(products_)


phone = input ("\n Enter your phone number (be sure number start with 0 and contain 10 digit): \n ")
name = input("Enter your name :\n ")
email = input("Enter your Emsil (#######@gmail.com ) :\n")
print("Enter your adress: \n")
city= input("  city:\n ")
quarter=input(" quarter: \n")
street=input("street : \n")


costumer = Costumer(cosumers ,phone,name,email,city,quarter, street)
costumer.add_costumer(phone,name,email,city,quarter, street)
costumer.check_phone(phone)
costumer.name_valid(name)

try:
	costumer.check_email(email)
except Exception as e:
	print(Fore.RED + e)



while True:
	print(Fore.RED , "menu")
	print(Style.RESET_ALL)
	try:
		choise = input("\n 1- Checken Burger \n 2- Meet Burger \n 3- display your order \nwrite \'E\' to exit the menu \n For evaluation press \'V\'  :) \n")
		
		if choise == "1":
			print(Style.RESET_ALL)

			product.request(choise)
			print(Fore.GREEN + "thank you dear \n Your order will be prepared immediately \n If you do not want to add more products, press E ")

			
		elif choise == "2":
			print(Style.RESET_ALL)

			product.request( choise)
			print(Fore.GREEN + "thank you dear \n Your order will be prepared immediately \n If you do not want to add more products, press E ")

		elif choise == "3":
			display1 = product.display(choise)
			print(display1)
			print(" \n Your price is 25.RS :) ")


		elif choise == "E":
			break
		
	#	else:
		#	print(Style.RESET_ALL)
		#	raise Exception (Fore.RED + "Please choise 1 or 2 \n 1 to checken burger \n 2 to meet burger ")
		elif choise == "V":
			v = input("How was the service from 1 to 5, where 1 was completely satisfied and 5 was not satisfied at all?")
			V = lambda v: print("We are happy for you, dear customer, and we wish you a nice day" , v)
			print(V(v))

		
	except ValueError: 
		print(Fore.RED + "Invalid input. Please enter a valid integer.") 
	except Exception as e :
		print(Fore.RED + e)

		


