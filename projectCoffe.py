from colorama import Fore, Back, Style

class DispenserCoffe:
    def __init__(self, name, cost,number_of_items) -> None:
        self.name = name
        self.cost=cost
        self.number_of_items=number_of_items

    def get_cost(self):
        return self.cost
    
    def get_name(self):
        return self.name

    def make_sale(self):
        if self.number_of_items > 0:
            self.number_of_items -= 1
        else:
            raise Exception("This Coffe is not available now.")
    
        

def sell_product(product): 
    money=0
    try:
        if product.get_cost() > 0 :  
            while money < product.get_cost():
                print(f"Please insert {product.get_cost() - money} Riyals to get your product:")
                money2 = int(input())
                money += money2

            if money == product.get_cost():
                product.make_sale()
                print(Fore.BLUE + "Please take your drink" + Style.RESET_ALL)
          
            elif money > product.get_cost():
                print(f"You have remaining of { money - product.get_cost()} Riyals for you to use!")
                print(Back.GREEN +"Do you want to continue?" + Style.RESET_ALL)
                print(Fore.BLUE +"(1) Yes"+Style.RESET_ALL)
                print(Fore.RED + "(2) No"+Style.RESET_ALL)
                in_more = int(input())

                if in_more == 1:
                    product.make_sale()
                    print(Fore.BLUE +"Please take your drink"+Style.RESET_ALL)
                else:
                    print(Fore.RED ,f"Please take back {money} Riyals"+Style.RESET_ALL)
    except ValueError as e:
        print(Fore.RED ,"We only accept riyals , try again "+Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + str(e) + Style.RESET_ALL)
        print(input("If you want a menu, click Enter"))

   



