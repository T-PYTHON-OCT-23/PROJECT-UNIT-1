from tabulate import *
from datetime import datetime
from art import *
from colorama import *

class PropertyData:
    def __init__(self,property_type:str,location:str,rooms:int,rent:float,occupancy:str,pay:str,start_date:datetime,end_date:datetime,rent_year:int,phone_number:int,tenant_name:str):
        self.property_type = property_type
        self.location=location
        self.__rooms=rooms
        self.__rent=rent
        self.__occupancy=occupancy
        self.__pay=pay
        self.__start_date=start_date
        self.__end_date = end_date
        self.__rent_year=rent_year
        self.__phone_number = phone_number
        self.tenant_name = tenant_name
    
    def set_rooms(self,rooms):
        if type(rooms) is not int:
            raise Exception(Fore.RED+"please only integer value!!"+Style.RESET_ALL)
        elif rooms < 0 or rooms > 20:
            raise Exception(Fore.RED+"please numbers of rooms between 1 - 20 !!"+Style.RESET_ALL)
        self.__rooms=rooms    
    def get_rooms(self):
        return self.__rooms
    def set_rent(self,rent):
        if type(rent) is not int :
            raise Exception(Fore.RED+"please only integer or float value!!"+Style.RESET_ALL)
        elif rent <= 0 :
            raise Exception(Fore.RED+ "please more than 0 !!" +Style.RESET_ALL)
        self.__rent=rent   
    def get_rent(self):
        return self.__rent
    def set_occupancy(self,occupancy):
        if type(occupancy) is not str:
            raise Exception(Fore.RED+"please only string value!!"+Style.RESET_ALL)
        elif occupancy.lower() != "empty" and occupancy.lower() != "not empty" :
            raise Exception(Fore.RED+"please just Empty or Not Empty!!"+Style.RESET_ALL)
        self.__occupancy=occupancy   
    def get_occupancy(self):
        return self.__occupancy
    def set_pay(self,pay):
        if type(pay) is not str:
            raise Exception(Fore.RED+"please only string value!!")
        elif pay.lower() != "pay" and pay.lower() != "not pay" and pay.lower() != "":
            raise Exception(Fore.RED+"please only Pay or Not Pay!!"+Style.RESET_ALL)
        
        self.__pay=pay    
    def get_pay(self):
        return self.__pay
    def set_start_date(self,start_date):
        if self.__start_date is not None:
            date_obj = datetime.strptime(start_date,"%d-%m-%Y")
            format_date = date_obj.strftime("%d %B %Y")
            
            self.__start_date = format_date
    def get_start_date(self):
        return self.__start_date
    def set_end_date(self,end_date):
        if self.__start_date is not None:
            date_obj = datetime.strptime(end_date,"%d-%m-%Y")
            format_date = date_obj.strftime("%d %B %Y")
        
            self.__end_date = format_date
    def get_end_date(self):
        return self.__end_date
    def set_rent_year(self,rent_year):
        if type(rent_year) is not int :
            raise ValueError(Fore.RED+"please only integer or float value!!"+Style.RESET_ALL)
        elif rent_year <= 0 :
            raise Exception(Fore.RED+"please more than 0 !!"+Style.RESET_ALL)
        self.__rent=rent_year  
    def get_rent_year(self):
        return self.__rent_year
    def set_phone(self,phone_number):
        if self.__phone_number is not None:
            if type(phone_number) is not int :
                raise ValueError(Fore.RED+"please only integer or float value!!"+Style.RESET_ALL)
            
            self.__phone_number=phone_number  
    def get_phone(self):
        return self.__phone_number