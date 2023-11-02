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
            raise Exception(Fore.RED +"The name must consist of letters")
        elif len(name) <= 4:
            raise Exception(Fore.RED +"Please enter a name that is four or more characters long")
        elif type(name[0]) != str:
            raise Exception(Fore.RED +"The first letter must not be a number or symbol")
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_email(self, email:str):
        if not email.endswith("@gmail.com") :
            raise Exception(Fore.RED +"The email must end with @gmail.com")
        elif not len(email) > 12:
            raise Exception(Fore.RED +"The email must contain more than 12 characters")
        elif not email.count("@") == 1:
            raise Exception(Fore.RED +"The email must contain @")
        elif not email.count(" ") == 0 :
             raise Exception(Fore.RED +"The email must not contain spaces")
        
            
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def set_password(self, password:str):
        if len(password) <= 4 :
            raise Exception(Fore.RED +"The password must be more than four")
            
        self.__password = password
        
    def get_password(self):
        return self.__password
    
    def set_points(self,points):
        self.__points = points
    
    def get_points(self):
        return self.__points
    