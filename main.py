import datetime   
from art import *  
from stringcolor import *            



listFoods= []                        
list_item_price = [0] * 100 
list_item_order = [0] * 100         


tprint("Welcome to Order System",font="blubhead")                                                                                                                  
def mainMenu():
    while True:                                           
        print("-" * 31 + "MAIN MENU" + "-" * 32 + "\n"     
              "\t(O) "+cs("ORDER","Aqua") +                            
              "\t(E) "+cs("EXIT","Red2") +
              "\t(A) "+cs("ADMIN","Blue2"),"\n"+
              "_" * 72)
        choice = str(input("Please Select Your Operation: ")).upper()                                           
        if (choice == 'O'):                                                                       
                order()                                       
                break 
        elif (choice == 'A'):                                                                       
                adminP()                                     
                break                                                                                                                                                         
        elif (choice == 'E'):                                        
                print("-" * 32 + "THANK YOU" + "-" * 31 + "\n")           
                break                                                    
        else:                                                                                   
                print(cs("\n""ERROR: Invalid Input (" + str(choice) + "). Try again!", "Red2"))      

def order():                                                                              
    while True:                                             
        print("-" * 31 + "ORDER PAGE" + "-" * 31 + "\n"    
              "\t(F) FOODS\n"
              "\t(M) MAIN MENU\n"
              "\t(E) "+cs("EXIT","Red2")+"\n" +
              "_" * 72)
        choice = str(input("Please Select Your Operation: ")).upper() 
        if (choice == 'F'): 
            food_order()
            break
        elif (choice == 'M'):
            mainMenu()
            break
        elif (choice == 'E'):
            print("-" * 32 + "THANK YOU" + "-" * 31 + "\n")
            break
        else:
            print(cs("ERROR: Invalid Input (" + str(choice) + "). Try again!", "Red2"))

def file_reader():                                                                        
    file_foods = open('list_foods.txt', 'r' ,encoding="utf-8") 
    for i in file_foods: 
        listFoods.append(str(i.strip())) 
    file_foods.close()

    i = 0
    while i <= (len(listFoods) - 1): 
        if '$' in listFoods[i]:
            listFoods[i] = str(listFoods[i][:listFoods[i].index('$') - 1]) + ' ' * (20 - (listFoods[i].index('$') - 1)) + str(listFoods[i][listFoods[i].index('$'):])
        i += 1
   
file_reader()

def food_order():
    while True:
            print("-" * 26 + "ORDER FOODS" + "-" * 26)
            print(" |NO| |FOOD NAME|         |PRICE|   ")
            i = 0
            while i < len(listFoods):
                var_space = 1
                if i <= 8:                   
                    var_space = 2

                if i < len(listFoods):
                    food = " (" + str(i + 1) + ")" + " " * var_space + str(listFoods[i]) + "  | " 
                else:
                    food = " " * 36 + "| " 
                print(food)
                i += 1
             
            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) "+cs("EXIT","Red2")+ "\n"+ "_" * 72)

            choice = input("Please Select Your Operation: ").upper()
            if (choice == 'M'):
                print("\n" * 1)
                mainMenu()
                break
            if (choice == 'P'):
                print("\n" * 1)
                payment() 
                break
            if (choice == 'E'):
                print("-" * 32 + "THANK YOU" + "-" * 31 + "\n") 
                break
            try:        
                int(choice)
                if (int(choice) <= len(listFoods) and int(choice) > 0) or (int(choice)):
                        print("\n" + "_" * 72 + "\n" + str(listFoods[int(choice) - 1])) 

                choice2 = input("How Many You Want to Order?: ").upper()
                if int(choice2) > 0:
                        list_item_order[int(choice) - 1] += int(choice2) # adding item to Orders Array
                        print(cs("Successfully Ordered!", "Green2"))
                        food_order()
                        break
                else:
                    print("\n" * 1 + "ERROR: Invalid Input (" + str(choice2) + "). Try again!")
            except:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(choice) + "). Try again!")

def report():
    while True:
        print("-" * 33 + "REPORT" + "-" * 33 + "\n")
        file_report = open('report.txt', 'r',encoding="utf-8").read()
        print(file_report)
        print("\n(M) MAIN MENU          (E)"+cs("EXIT","Red2") +"\n" + "_" * 72)
        choice = str(input("Please Select Your Operation: ")).upper()
        if (choice == 'M'):
            mainMenu()
            break
        elif (choice == 'E'):
            print("-" * 32 + "THANK YOU" + "-" * 31 + "\n")
            break
        else:
            print(cs("ERROR: Invalid Input (" + str(choice) + "). Try again!", "Red2"))

def payment():
    while True:
        print("-" * 32 + "PAYMENT" + "-" * 33 + "\n") 
        #total_price = 0 
        report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE:" + str(datetime.datetime.now())[:19] + "\n" + " " * 17 + "-" * 35 
        item = 0
        while item < len(list_item_order): 
            if(list_item_order[item] != 0):
                if (item >= 0) and (item < 60):
                    report_new +=  "\n" + " " * 17 + str(listFoods[item]) + "  x  " + str(list_item_order[item]) 
                    print(" " * 17 + str(listFoods[item]) + "  x  " + str(list_item_order[item])) 
                    price = list_item_price[item]
                    quntitiy = list_item_order[item]
                    total_price = lambda price , quntitiy : price * quntitiy
                item += 1
            else:
                item += 1
        print("\n (P) PAY           (M) MAIN MENU           (R) REPORT          (E) "+cs("EXIT","Red2")+"\n" + "_" * 72)
     
        choice = str(input("Please Select Your Operation: ")).upper()
        if (choice == 'P'):
            print("\n" * 1)
            print(cs("Successfully Paid!", "Green2")) 
            file_report = open('report.txt', 'a',encoding="utf-8") 
            file_report.write(report_new)
            file_report.close()
            break
        elif (choice == 'M'):
            print("\n" * 1)
            mainMenu() 
            break
        elif (choice == 'R'):
            print("\n" * 1)
            report() 
            break
        elif ('E' in choice) or ('e' in choice):
            print("-" * 32 + "THANK YOU" + "-" * 31 + "\n")
            break
        else:
            print(cs("ERROR: Invalid Input (" + str(choice) + "). Try again!", "Red2"))


def adminP (): 
        password = input("Please enter the password for admin : ")
        if (len(password) ==4):
         while True:
            if (password=='0000'):
                tprint("Welcome to Admin page",font="doom")
                print("-" * 31+ "-" * 20 + "\n"    
              "\t(AF) ADD FOOD \n"
              "\t(RF) REMOVE FOOD \n"
              "\t(LM) LIST MENU\n"
              "\t(E) "+cs("EXIT","Red2")+"\n" +
              "_" * 72)
                
            x = str(input("Please Select Your Operation: ")).upper() 
            if x == "AF":
                item = input("Fill in the menu: ")
                with open("list_Foods.txt", "a", encoding="utf-8") as file:
                    file.write(item + "\n")
                    #listFoods.append(item)
                    print(cs("Added item successfully !","Green2")+"\n")
                ans=input("do you want any thing else ? ").upper()
                if ans =="YES":
                        adminP()
                elif ans =="NO":
                    mainMenu()
                    break

            elif x=="RF":
                with open("list_foods.txt", "r") as f: 
                    data = f.readlines() 
                with open("list_foods.txt", "w") as f: 
                    item = input("Fill what do you want to remove : ")
                    for line in data : 
                     if line.strip("\n") != item :  
                      f.write(line)
                    print(cs("Removed item successfully !","Green2")+"\n")
                ans=input("do you want any thing else ? ").upper()
                if ans =="YES":
                    adminP()
                elif ans =="NO":
                    mainMenu()
                break

            elif x == "LM":
                with open("list_Foods.txt", "r", encoding="utf-8") as file:
                 content = file.read()
                print(content)
                ans=input("do you want any thing else ? ").upper()
                if ans =="YES":
                    adminP()
                elif ans =="NO":
                    mainMenu()
                break
            elif x == "E":
                print("good bye!")
                mainMenu()
            break
        else:                                                                                   
         print(cs("\n""ERROR: Invalid Password. Try again!", "Red2"))  
       
mainMenu()

