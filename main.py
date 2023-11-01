from projectCoffe import*
      
listCoffee=[]
listCoffee.append(DispenserCoffe("Latte",15, 2))
listCoffee.append( DispenserCoffe("Cappacino", 18, 100))
listCoffee.append(DispenserCoffe("BlackCoffee", 9, 100))
listCoffee.append(DispenserCoffe("Tea", 5, 100))


def add_prodructs(user , password):
    user= "Reef"
    password="12346Rr"
    name_prducts=input("Enter the products name to want add to list: ")
    number_priducts=int(input("Enter the  number of the products : ")) 
    cost= int(input("Enter the price for product : ")) 
    listCoffee.append(DispenserCoffe(name_prducts,cost,number_priducts))

while True:
    print("-"*50)
    print(Back.CYAN +"*** Welcome to Coffe vending Machine ***"+Style.RESET_ALL)
    print("To select an item, enter ")

    counter = 1
    for coffee in listCoffee:
        print(f"-{counter} for {coffee.name}")
        counter += 1

    print(f"-{counter} for show the number of remaining cups for each type of coffee ")
    print(f"-{counter+1} To display products by price ")
    print(f"-{counter+2} To want add products, Only for the manager")
    print(f"-{counter+3} To exit")
    option = int(input("Enter your option: "))
    

    if option <= len(listCoffee):
        sell_product(listCoffee[option-1])
    elif option == counter:
        count=1
        for items in listCoffee:
            print(f"The number of {items.name} is  {items.number_of_items}")

    elif option == counter+1:
        print("products sorted by price from low to high:")
        newlist=[]
        for i in listCoffee:
            newlist.append({"name":i.get_name(),"cost":int(i.get_cost())})

        newlist.sort(key=lambda item:item["cost"])
        print(newlist)
        
        for index, i in enumerate(newlist):
            print(f"{index+1}- {i['name']} Its cost {i['cost']}")
    
    elif option==counter+2:
        user =input(" Enter the user: ")
        password=input("Enter the password: ")

        if user =="Reef" and password=="12346Rr":
            add_prodructs(user,password)
        else:
            print("You are not allowed to add")
        
    elif option== counter+3:
        print("Goodbye")
        break

    else:
        print("Your choice is incorrect, try again")
        