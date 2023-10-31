import json
from functools import reduce
from tabulate import tabulate
from art import *
from colorama import *
import random

class PropertyManager:
    def __init__(self , file_path):
        self .file_path = file_path
        self.properties = self.load_properties()
    def load_properties(self):
        try:
            with open(self.file_path, "r" , encoding="utf-8") as file:
                data = json.load(file)
                return data["properties"]
        except Exception as e:
            print(e)
            return []
    def save_properties(self):
        data = {"properties":self.properties}
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data,file)
    def add_property(self, property_data):
        id_list=[]
        while True:
            proper_id = random.randint(1, 1000)
            if proper_id not in id_list:
                break
        id_list.append(proper_id)
        for i in id_list:
            property_data["id"]= i
          
        self.properties.append(property_data)        
        self.save_properties()
        print(Fore.GREEN+"Property add succsufly"+Style.RESET_ALL)  
    def display_property(self):
        if not self.properties:
            print(Fore.RED+"No properties available"+Style.RESET_ALL)
        else:
            table=[]
            for propert in self.properties:
                
                table.append([
                propert['id'],propert['type'],
                propert['location'],
                propert['rooms'],
                propert['rent_ber_month'],
                propert['rent_ber_year'],
                propert['occupancy'],
                propert['pay'],
                propert['start_date'],
                propert['end_date'],
                propert['phone_number'],
                propert["tenant_name"]
                ])
        headers = ["ID","Type", "Location", "Rooms", "Rent -Month-", "The Remaining Rent -Year-", "Occupancy", "Pay", "Start Date", "End Date","Tenant Phone Number","Tenant Name"]
        print(tabulate(table, headers=headers , tablefmt='plain'))


    def get_property(self, propery_id):
        found_property = list(filter(lambda item: item["id"] == propery_id, self.properties))
        if len(found_property) > 0:
            return found_property[0]
        else:
            raise Exception("Not found")
        
    def update_property(self, property_id,ubdate_data):
        for propert in self.properties:
            if propert["id"] == property_id:
                propert.update(ubdate_data)
                self.save_properties() 
        print(Fore.GREEN+"Update succsufly"+Style.RESET_ALL)
    def delete_property(self, property_id):
        for propert in self.properties:
            if propert["id"] == property_id:
                
                len(self.properties)-1
                self.properties.remove(propert)
                self.save_properties()
        print(Fore.GREEN+"Delete succsufly"+Style.RESET_ALL)
    def search_properties(self, search_criteria):
        search_results = []
        for propert in self.properties:
            if search_criteria.capitalize() in propert.values():
                search_results.append(propert)
        if search_results:
            print(Fore.GREEN + f"Search results for '{search_criteria}':" + Style.RESET_ALL)
            table=[]
            for propert in search_results:
                     table.append([
                propert['id'],propert['type'],
                propert['location'],
                propert['rooms'],
                propert['rent_ber_month'],
                propert['rent_ber_year'],
                propert['occupancy'],
                propert['pay'],
                propert['start_date'],
                propert['end_date'],
                propert['phone_number'],
                propert["tenant_name"]
                ])
            headers = ["ID","Type", "Location", "Rooms", "Rent (Month)", "Rent (Year)", "Occupancy", "Pay", "Start Date", "End Date","Tenant Phone Number","Tenant Name"]
            print(tabulate(table, headers=headers,tablefmt="fancy_grid"))
    
        else:
            print(Fore.RED + f"No results found for '{search_criteria}'."+Style.RESET_ALL)
                   
    def calculate_total_price(self):
        list_rent =[]
        for i in self.properties:
            for key,value in i.items():
                if key=="pay" and value == "pay":
                    for key,value in i.items():
                        if key == "rent_ber_month":
                            list_rent.append(value)
                            list_rent
                            f = lambda x, y: x+y
                            sum = reduce(f, list_rent)
        total = sum
        table = tabulate([['Total Rent', total]], headers='keys', tablefmt='fancy_grid')
        print(table)            
        
    def calculate_not_pay(self):
        list_not_pay=[]
        for i in self.properties:
            if i["pay"]=="not pay":
                list_not_pay.append(i)
            #else:
                #print(Fore.RED+"All property Paid or not rented!!"+Style.RESET_ALL)    
                
        table = tabulate(list_not_pay, headers="keys", tablefmt="fancy_grid")
        print(table)