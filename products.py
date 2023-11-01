from colorama import Fore, Back, Style


class Product:
    

    def __init__(self, products_) -> None:

      self.products_ = products_
      self.dic_copy = self.products_["checken_burger"].copy()
      self.dic_copy1 = self.products_["meet_burger"].copy()



    def request (self, request):
        '''this funcaion take the details of the order'''

        

        if request == "1":
            print("555", self.dic_copy)
            want_cheese = input ("want a cheese? if Yes write \"Y\" if No write \"N\" ")
            if want_cheese == "Y":
              #self.dic_copy["checken_burger"]["cheese"] = True
              self.dic_copy["cheese"] = True

            elif want_cheese == "N":
              #self.dic_copy["checken_burger"]["cheese"] = False
              self.dic_copy["cheese"] = False


            want_lettuce = input ("want a lettuce? if Yes write \"Y\" if No write \"N\" ")
            if want_lettuce  == "Y":
             #self.dic_copy["checken_burger"]["lettuce"] = True
             self.dic_copy["lettuce"] = True

            elif want_lettuce == "N":
              #self.dic_copy["checken_burger"]["lettuce"] = False
              self.dic_copy["lettuce"] = False


            want_mayonnaise=input("want a mayonnaise? if Yes write \"Y\" if No write \"N\"")
            if want_mayonnaise  == "Y":
             # self.dic_copy["checken_burger"]["mayonnaise"] = True
              self.dic_copy["mayonnaise"] = True

            elif want_mayonnaise == "N":
              #self.dic_copy["checken_burger"]["mayonnaise"] = False
              self.dic_copy["mayonnaise"] = False


            want_meal =input("want a meal? if Yes write \"Y\" if No write \"N\"")
            if want_meal  == "Y":
              #self.dic_copy["checken_burger"]["meal"] = True
              self.dic_copy["meal"] = True
              return self.dic_copy.items() , "Your price is 25.RS :) "


            elif want_meal == "N":
              #self.dic_copy["checken_burger"]["meal"] = False
              self.dic_copy["meal"] = False

              return self.dic_copy.items() , "Your price is 15.RS :) "
        
        

        if request == "2":
            want_cheese = input ("want a cheese? if Yes write \"Y\" if No write \"N\" ")
            if want_cheese == "Y":
              #self.dic_copy1["meet_burger"]["cheese"] = True
              self.dic_copy1["cheese"] = True

            elif want_cheese == "N":
              #self.dic_copy1["meet_burger"]["cheese"] = False
              self.dic_copy1["cheese"] = False


            want_lettuce = input ("want a lettuce? if Yes write \"Y\" if No write \"N\" ")
            if want_lettuce  == "Y":
             #self.dic_copy1["meet_burger"]["lettuce"] = True
             self.dic_copy1["lettuce"] = True

            elif want_lettuce == "N":
              #self.dic_copy1["meet_burger"]["lettuce"] = False
              self.dic_copy1["lettuce"] = False


            want_mayonnaise=input("want a mayonnaise? if Yes write \"Y\" if No write \"N\"")
            if want_mayonnaise  == "Y":
             # self.dic_copy1["meet_burger"]["mayonnaise"] = True
              self.dic_copy1["mayonnaise"] = True

            elif want_mayonnaise == "N":
             # self.dic_copy1["meet_burger"]["mayonnaise"] = False
              self.dic_copy1["mayonnaise"] = False


            want_meal =input("want a meal? if Yes write \"Y\" if No write \"N\"")
            if want_meal  == "Y":
              #self.dic_copy1["meet_burger"]["meal"] = True
              self.dic_copy1["meal"] = True
              return self.dic_copy1.items() , "Your price is 25.RS :) "


            elif want_meal == "N":
              #self.dic_copy1["meet_burger"]["meal"] = False
              self.dic_copy1["meal"] = False
              return self.dic_copy1.items() , "Your price is 15.RS :) "
    
        else:
          raise Exception(Fore.RED + "\n Try again with a valid option please :(  \n")
          
      
      
    def display(self, request):
      '''this funcaion display the details of the order'''


      if request == "3":
        #p="Your price is 25.RS :)"
        for c in self.products_["checken_burger"]:
          #print(self.dic_copy)
          if len( self.dic_copy.items()) != 0:
            return list(self.dic_copy.items()) 
        for i in self.products_["meet_burger"]:
          if len(self.dic_copy1.items() ) != 0:
            return list(self.dic_copy1.items()) 
       



    

    

