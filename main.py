from property_manager_class import PropertyManager
from prpoerty_data_class import PropertyData
from tabulate import *
from art import *
from colorama import *
from datetime import datetime
import random
def display_menu():
    try:
        tprint("--------------------------",font="block-medium")
        tprint("Property Management System",font="block-medium")
        menu_items = [
        ["1.", "View Properties"],
        ["2.", "Add Property"],
        ["3.", "Update Property"],
        ["4.", "Delete Property"],
        ["5.", "Search Properties"],
        ["6.", "Total Rents Paid"],
        ["7.", "The Property That Not Pay"],
        ["8", "Exit"]
    ]
        table = tabulate(menu_items, headers=["Option", "Menu Item"], tablefmt="fancy_grid")
        print(table)
    except Exception as e:
        print(Fore.RED+e+Style.RESET_ALL)

def get_property_details():
    property_type = input("Property Type: ")
    location = input("Property Location: ")
    rooms= int(input("Number of Rooms: "))
    rent = int(input("rent ber month: "))
    rent_year = rent*12 #int (input("rent ber year"))
    occupancy = input("Is this property available?: write Empty or Not Empty: ")
    if occupancy.lower() == "not empty":
        tenant_name = input("Enter the tenant's name: ")
        phone_number =int(input("Enter the tenant's phone number:+966"))
        start_date = input("Enter the contract start date in the following (dd-mm-yyyy): ")
        end_date = input("Enter the contract end date in the following (dd-mm-yyyy): ")
        pay =  input("Has the rent been paid for this property?: Write Pay or Not Pay: ")
        

    else:
        start_date= None
        end_date=None
        pay = ""
        phone_number = None
        tenant_name = ""

    data = PropertyData(property_type,location,rooms,rent,occupancy,pay,start_date,end_date,rent_year,phone_number,tenant_name)
    data.set_rooms(rooms)
    data.set_rent(rent)
    data.set_rent_year(rent_year)
    data.set_occupancy(occupancy)
    data.set_pay(pay)
    data.set_start_date(start_date)
    data.set_end_date(end_date)
    data.set_phone(phone_number)
    data.get_rooms()
    data.get_rent()
    data.get_rent_year()
    data.get_occupancy()
    data.get_pay()
    data.get_start_date()
    data.get_end_date()
    data.get_phone()
    

        
    return {
        "type": property_type,
        "location": location,
        "rooms": rooms,
        "rent_ber_month": rent,
        "rent_ber_year": rent_year,
        "occupancy": occupancy,
        "pay":pay,
        "start_date": start_date,
        "end_date" :end_date,
        "phone_number": phone_number,
        "tenant_name": tenant_name
        }
        


def update_property_details(property_data):
    while True:
        tprint("Enter your choice  (1-8) To Update",font="cybermedum")
        menu_items = [
            ["1.", "Ubdate Rent"],
            ["2.", "Ubdate Occupancy"],
            ["3.", "Update Pay"],
            ["4.", "Update Start date"],
            ["5.", "Update End date"],
            ["6.", "Ubdate Tenant Phone Number"],
            ["7.", "Ubdate Tenant Name"],
            ["8.", "Exit"]
            
        ]
        table = tabulate(menu_items, headers=["Option", "Menu Item"], tablefmt="fancy_grid")
        print(table)
        choice=input("Enter your choice (1-8): ")
        if choice == "1":
            price = input("do price:")
            property_data["rent_ber_month"]= price
            return property_data
        elif choice == "2":
                occupancy = input("Enter pay update onle (Empty) or (Not Empty):")
                property_data["occupancy"]= occupancy
                return property_data
        elif choice == "3":
            pay = input("Enter occupancy update onle (Pay) or (Not Pay) or (): ")
            property_data["pay"]= pay
            return property_data    
        elif choice == "4":
            start_date = input("Enter update start date in the following (dd-mm-yyyy): ")
            property_data["start_date"]= start_date
            return property_data 
        elif choice == "5":
            end_date = input("Enter update end date in the following (dd-mm-yyyy): ")
            property_data["end_date"]= end_date
            return property_data 
        elif choice == "6":
            phone = input("Enter update tenant phone number: ")
            property_data["phone_number"]= phone
            return property_data
        elif choice == "7":
            name = input("Enter update tenant name: ")
            property_data["tenant_name"]= name
            return property_data  
        elif choice == "8":
            tprint("Update Done!!",font="block-medium")
            break        
        else:
            print(Fore.RED+"Error Choice"+Style.RESET_ALL)
def get_property_id():
    return int(input("Enter Property ID: "))

def search_properties():
    search_criteria = input("Enter search term: ")
    return search_criteria
def main():
    property_manager = PropertyManager("property_data.json")
    print(Fore.BLUE)
    print(Back.WHITE)
    display_menu()
    while True:
        print(Fore.BLUE)
        print(Back.WHITE)
        tprint("Enter your choice (1-8): ",font="cybermedum")
        choice = input("Enter your choice (1-8): ")
        try:
            if choice == "1":
                try:
                    property_manager.display_property()
                    choice=input("If you want show the list of choic agine enter (yes) or press any key to continue: ")
                    if choice.lower() == "yes":
                        display_menu()
                except Exception as e:
                    print(e)
            elif choice == "2":
                try:
                    property_data = get_property_details()
                    property_manager.add_property(property_data)
                    choice=input("If you want show the list of choic agine enter (yes) or press any key to continue: ")
                    if choice.lower() == "yes":
                        display_menu()
                except Exception as e:
                    print(e)
            elif choice == "3":
                try:
                    property_id = get_property_id()
                    found_property = property_manager.get_property(property_id)
                    property_data = update_property_details(found_property)
                    property_manager.update_property(property_id, property_data)
                    choice=input("If you want show the list of choic agine enter (yes) or press any key to continue: ")
                    if choice.lower() == "yes":
                        display_menu()
                except Exception as e:
                    print(e)
            elif choice == "4":
                try:
                    property_id = get_property_id()
                    property_manager.delete_property(property_id)
                    choice=input("If you want show the list of choic agine enter (yes) or press any key to continue: ")
                    if choice.lower() == "yes":
                        display_menu()
                except Exception as e:
                    print(e)
            elif choice == "5":
                try:
                    search_criteria = search_properties()
                    property_manager.search_properties(search_criteria)
                    choice=input("If you want show the list of choic agine enter (yes) or press any key to continue: ")
                    if choice.lower() == "yes":
                        display_menu()
                except Exception as e:
                    print(e)
            elif choice == "6":
                try:
                    property_manager.calculate_total_price()
                    choice=input("If you want show the list of choic agine enter (yes): ")
                    if choice.lower() == "yes":
                        display_menu()
                except Exception as e:
                    print(e)
            elif choice == "7":
                try:
                    property_manager.calculate_not_pay()
                    choice=input("If you want show the list of choic agine enter (yes): ")
                except Exception as e:
                    print(e)           
            elif choice == "8":
                tprint("Goodbye!",font="block-medium")
                break
            else:
                print(Fore.RED+"Invalid choice. Please try again."+Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED+e+Style.RESET_ALL)
main() 