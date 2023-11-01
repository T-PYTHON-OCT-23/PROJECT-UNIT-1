from colorama import Fore, Back, Style,init
import hashlib
init(autoreset=True)

class Clint:
    def __init__(self , name:str , email:str,password:str, points:int=0) -> None:
        self.__name= name
        self.__email= email
        self.__password = password
        self.__points = points
        
    def set_name(self, name:str):
        if type(name) != str:
            Exception(Fore.RED +"The name must consist of letters")
        elif len(name) <= 4:
            Exception(Fore.RED +"Please enter a name that is four or more characters long")
        elif type(name[0]) != str:
            Exception(Fore.RED +"The first letter must not be a number or symbol")
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_email(self, email:str):
        if email.endswith("@gmail.com") and len(email) > 12 and email.count("@") == 1 and email.count(" ") == 0:
            raise Exception(Fore.RED +"The email must not contain spaces and end with @gmail.com")
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def set_password(self, password:str):
        if len(password) <= 4 :
            raise Exception(Fore.RED +"The password must be more than four")
        elif (not password in str or int) :
            raise Exception(Fore.RED +"The password must contain letters and numbers")
            
        self.__password = password
        
    def get_password(self):
        return self.__password
    
    def set_points(self,points):
        self.__points = points
    
    def get_points(self):
        return self.__points
    