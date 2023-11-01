from projectCoffe import*
    
    
listCoffe=["count","Latte","Cappacino","BlackCoffee","Tea"]
listCoffe[1] = DispenserCoffe(5, 2)
listCoffe[2] = DispenserCoffe(5, 100)
listCoffe[3] = DispenserCoffe(5, 100)
listCoffe[4] = DispenserCoffe(5, 100)

while True:
    print("-"*50)
    print(Back.CYAN , "*** Welcome to Coffe vending Machine ***",Style.RESET_ALL)
    print("To select an item, enter ")
    print("-1 for Latte")
    print("-2 for Cappacino")
    print("-3 for BlackCoffee")
    print("-4 for Tea") 
    print("-5 for show the number of remaining cups for each type of coffee ")
    print("-6 to exit")
    option = int(input("Enter your option: "))
    

    if option == 1:
        sell_product(listCoffe[1], listCoffe[0])
    elif option == 2:
        sell_product(listCoffe[2], listCoffe[0])
    elif option == 3:
        sell_product(listCoffe[3], listCoffe[0])
    elif option == 4:
        sell_product(listCoffe[4], listCoffe[0])
    elif option==5:
        print("The number of Latte left is:", listCoffe[1].get_no_of_items())
        print("The number of Cappacino left is:", listCoffe[2].get_no_of_items())
        print("The number of Black Coffee left is:", listCoffe[3].get_no_of_items())
        print("The number of Tea left is:", listCoffe[4].get_no_of_items())
        print(input())
    elif option==6:
        print("Goodbye")
        break
    else:
        print("Your choice is incorrect, try again")
        