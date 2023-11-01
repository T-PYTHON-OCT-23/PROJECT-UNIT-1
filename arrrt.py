from fun import *
format_dt = lambda dt: dt.strftime("%Y-%m-%d %H:%M")
dt = datetime.now()
formatted_dt = format_dt(dt)
print("The Time Now ", formatted_dt)
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
        print("1. Toyota\n2. Nissan\n3. Hyundai")
        brand_number = input("Enter the number of the brand: ")
        brand_dict = {"1": "Toyota", "2": "Nissan", "3": "Hyundai"}
        if brand_number in brand_dict:
            brand = brand_dict[brand_number]
            part = input("Enter the name of the spare part: ")
            price = int(input("Enter the price of the spare part: "))
            if brand in spare_parts:
                spare_parts[brand][part] = price
                print(Fore.GREEN + f"Spare part {part} added successfully to {brand}.")
            else:
                print(f"Invalid brand: {brand}")
        else:
            print("Invalid number. Please try again.")
    else:
        print("You are not authorized to add spare parts.")



def remove_spare_parts():
    if authenticate():
        print("Welcome, Naif Manager", art_2)
        print("1. Toyota\n2. Nissan\n3. Hyundai")
        brand_number = input("Enter the number of the brand: ")
        brand_dict = {"1": "Toyota", "2": "Nissan", "3": "Hyundai"}
        if brand_number in brand_dict:
            brand = brand_dict[brand_number]
            print("Spare parts:")
            for i, part in enumerate(spare_parts[brand], start=1):
                print(f"{i}. {part}")
            part_number = int(input("Enter the number of the spare part to remove: "))
            part = list(spare_parts[brand].keys())[part_number - 1]
            del spare_parts[brand][part]
            print(Fore.GREEN + f"Spare part {part} removed successfully from {brand}.")
        else:
            print("Invalid number. Please try again.")
    else:
        print(Fore.RED + "You are not authorized to remove spare parts.")


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
    print("1. Toyota\n2. Nissan\n3. Hyundai")
    brand_number = input("Enter the number of the brand: ")
    brand_dict = {"1": "Toyota", "2": "Nissan", "3": "Hyundai"}
    if brand_number in brand_dict:
        brand = brand_dict[brand_number]
        print("Available parts:")
        table = PrettyTable(['Part Number', 'Part', 'Price'])
        for i, (part, price) in enumerate(spare_parts[brand].items(), start=1):
            table.add_row([i, part, price])
        print(table)
        parts_numbers = input("Enter the numbers of the spare parts separated by commas: ").split(',')
        total_cost = 0
        invoice_parts = []
        for part_number in parts_numbers:
            part_number = int(part_number.strip()) - 1
            if part_number < len(spare_parts[brand]):
                part = list(spare_parts[brand].keys())[part_number]
                total_cost += spare_parts[brand][part]
                sales.append((brand, part, spare_parts[brand][part]))
                invoice_parts.append((part, spare_parts[brand][part]))
            else:
                print(f"Invalid spare part number: {part_number + 1}")
        print("\nInvoice:")
        for part, price in invoice_parts:
            print(f"{part}: ${price}")
        print(f"Total cost: ${total_cost}")
    else:
        print("Invalid number. Please try again.")


def create_sales_report():
    if authenticate():
        print("Welcome, Naif Manager", art_2)
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
        list(map(lambda item: table_brand.add_row([item[0], f"${item[1]}"]), sales_by_brand.items()))
        print(table_brand)

        print("\nSales by part:")
        table_part = PrettyTable()
        table_part.field_names = ["Part", "Sales"]
        list(map(lambda item: table_part.add_row([item[0], f"${item[1]}"]), sales_by_part.items()))
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