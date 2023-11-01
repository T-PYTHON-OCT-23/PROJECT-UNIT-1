from colorama import Fore, Back, Style


class Costumer:




    def __init__(self , cosumers , phone_number,name,email ,city ,quarter, street):
        self.cosumers = cosumers.copy()
        self.phone_number = phone_number
        self.name = name
        self.email = email
        self.city = city
        self.quarter = quarter
        self.street = street


    def add_costumer(self , phone_number,name,email ,city ,quarter, street):
        '''this funcation add costumer information '''
        self.cosumers["phone_number"] = phone_number
        self.cosumers["name"] = name
        self.cosumers["email"] = email
        self.cosumers["city"] = city
        self.cosumers["quarter"] = quarter
        self.cosumers["street"] = street
        return self.cosumers
    
    def check_phone (self , phone_number):
        '''this funcaion check if phone number is valid or invalid'''
        if len(phone_number) >10 or len(phone_number) <10 or not phone_number.isdigit():
            raise Exception( Fore.RED + "\n The number is invalid , Try again :(  \n")


        elif len(phone_number) ==10 and phone_number.isdigit():
            print( Fore.GREEN + "\n Succssfly add number \n ")
            print(Style.RESET_ALL)


    def name_valid(self , name):
        '''this funcaion check if name is valid or invalid'''

        if isinstance(name , str):
            print( Fore.GREEN + "\n Succssfly add Name \n ")
            print(Style.RESET_ALL)

        else:
            raise Exception( Fore.RED + "\n The Name is invalid , Try again :(  \n")
        print(Style.RESET_ALL)


    def check_email(self , email):
        '''this funcaion check if Email is valid or invalid'''


    
        if email.find("@") < 0:
            raise Exception(Fore.RED + "not valid email")
        
        name_part , domain = email.split("@", maxsplit=1) 
        if len(name_part) !=0 or len(domain) !=0:
            print( Fore.GREEN + "\n Succssfly add Email \n ")
            print(Style.RESET_ALL)

        else:
            raise Exception(Fore.RED + "\n The Email is invalid , Try again :(  \n")
        print(Style.RESET_ALL)





