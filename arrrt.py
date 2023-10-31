from fun import *
dt = datetime.datetime.now()
dt = dt.strftime("%Y-%m-%d %H:%M")
print("The Time Now ",dt)
spare_parts
Car
manager_account
def authenticate():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == manager_account["username"] and password == manager_account["password"]:
        return True
    else:
        print("Invalid username or password.")
        aprint("happy")
        return False
def add_spare_parts():
    if authenticate():
        print("Welcome, Naif Manager", art_2)
        brand = input("Enter the brand (Toyota, Nissan, Hyundai): ").capitalize()
        part = input("Enter the name of the spare part: ")
        price = int(input("Enter the price of the spare part: "))
        if brand in spare_parts:
            spare_parts[brand][part] = price
        else:
            print(f"Invalid brand: {brand}")
    else:
        print("You are not authorized to add spare parts.")

def remove_spare_parts():
    if authenticate():
        print("Welcome, Naif Manager", art_2)
        brand = input("Enter the brand (Toyota, Nissan, Hyundai): ").capitalize()
        part = input("Enter the name of the spare part to remove: ")
        if brand in spare_parts and part in spare_parts[brand]:
            del spare_parts[brand][part]
            print(f"Spare part {part} removed successfully from {brand}.")
        else:
            print(f"Invalid brand or spare part: {brand}, {part}")
    else:
        print("You are not authorized to remove spare parts.")

def print_menu():
    print("🚗💨 Welcome to the Spare Parts Program for Toyota, Nissan, and Hyundai Cars! 🎉🔧")
    print(Style.DIM + "Please select an option:")
    print(Style.DIM + "1.View spare parts for Toyota cars 🚗")
    print(Style.DIM + "2.View spare parts for Nissan cars 🚗")
    print(Style.DIM + "3.View spare parts for Hyundai cars 🚗")
    print(Style.DIM + "4.Purchase spare parts 🛒")
    print(Fore.RED + "5.Add new spare parts (Manager only) ➕")
    print(Fore.RED + "6.Remove spare parts (Manager only) ➖")
    print(Fore.RED + "7.Create sales report (Manager only) 📊")
    print("8.Exit 🚪")
    print(Style.RESET_ALL)

sales = []
def purchase_spare_parts():
    brand = input("Enter the brand (Toyota, Nissan, Hyundai): ").capitalize()
    parts = input("Enter the names of the spare parts separatnaied by commas: ").split(',')
    total_cost = 0
    for part in parts:
        part = part.strip()
        if brand in spare_parts and part in spare_parts[brand]:
            total_cost += spare_parts[brand][part]
            sales.append((brand, part, spare_parts[brand][part]))
        else:
            print(f"Invalid spare part: {part}")
    return total_cost


def create_sales_report():
    if authenticate():
        total_sales = sum(price for brand, part, price in sales)
        print(f"Total sales: ${total_sales}\n")

        sales_by_brand = {}
        sales_by_part = {}
        for brand, part, price in sales:
            if brand not in sales_by_brand:
                sales_by_brand[brand] = 0
            sales_by_brand[brand] += price

            if part not in sales_by_part:
                sales_by_part[part] = 0
            sales_by_part[part] += price

        print("Sales by brand:")
        table_brand = PrettyTable()
        table_brand.field_names = ["Brand", "Sales"]
        for brand, brand_sales in sales_by_brand.items():
            table_brand.add_row([brand, f"${brand_sales}"])
        print(table_brand)

        print("\nSales by part:")
        table_part = PrettyTable()
        table_part.field_names = ["Part", "Sales"]
        for part, part_sales in sales_by_part.items():
            table_part.add_row([part, f"${part_sales}"])
        print(table_part)



def main():
    while True:
        print_menu()
        choice = input(Style.DIM + "Enter your choice: ")
        try:
            if choice == "1":
                Car('Toyota',spare_parts['Toyota']).view_spare_parts()
                
            elif choice == "2":
                Car('Nissan',spare_parts['Nissan']).view_spare_parts()
                
            elif choice == "3":
                Car('Hyundai',spare_parts['Hyundai']).view_spare_parts()
                
            elif choice == "4":
                total_cost = purchase_spare_parts()
                print(f"The total cost of your purchase is ${total_cost}.")
                
            elif choice == "5":
                add_spare_parts()
                
            elif choice == "6":
                remove_spare_parts()
                
            elif choice == "7":
                create_sales_report()
                
            elif choice == "8":
                print("Thank you, goodbye", art_2)
                sys.exit(0)
        
            else:
                        raise TypeError("Invalid choice. Please try again.")
        except ValueError as e:
                    print(e)
        except TypeError as e:
                    print(e)
        except Exception as e:
                    print(e)
main()