from colorama import Fore, Back, Style


class Product:
    

    def __init__(self, products_) -> None:

      self.products_ = products_
      self.dic_copy = self.products_["checken_burger"].copy()
      self.dic_copy1 = self.products_["meet_burger"].copy()
      self.order=0



    def request (self, request):
        '''this funcaion take the details of the order'''

        

        if request == "1":
            self.order=1
            #print( self.dic_copy)
            want_cheese = input ("want a cheese? if Yes write \"Y\" if No write \"N\" \n")
            if want_cheese.lower() == "y":
              #self.dic_copy["checken_burger"]["cheese"] = True
              self.dic_copy["cheese"] = True

            elif want_cheese.lower() == "n":
              #self.dic_copy["checken_burger"]["cheese"] = False
              self.dic_copy["cheese"] = False


            want_lettuce = input ("want a lettuce? if Yes write \"Y\" if No write \"N\" \n")
            if want_lettuce.lower()  == "y":
             #self.dic_copy["checken_burger"]["lettuce"] = True
             self.dic_copy["lettuce"] = True

            elif want_lettuce.lower() == "n":
              #self.dic_copy["checken_burger"]["lettuce"] = False
              self.dic_copy["lettuce"] = False


            want_mayonnaise=input("want a mayonnaise? if Yes write \"Y\" if No write \"N\" \n")
            if want_mayonnaise.lower()  == "y":
             # self.dic_copy["checken_burger"]["mayonnaise"] = True
              self.dic_copy["mayonnaise"] = True

            elif want_mayonnaise.lower()== "n":
              #self.dic_copy["checken_burger"]["mayonnaise"] = False
              self.dic_copy["mayonnaise"] = False


            want_meal =input("want a meal? if Yes write \"Y\" if No write \"N\" \n ")
            if want_meal.lower()  == "y":
              #self.dic_copy["checken_burger"]["meal"] = True
              self.dic_copy["meal"] = True
              return self.dic_copy.items() , "Your price is 25.RS :) "


            elif want_meal.lower() == "n":
              #self.dic_copy["checken_burger"]["meal"] = False
              self.dic_copy["meal"] = False

              return self.dic_copy.items() , "Your price is 15.RS :) "
        
        

        if request == "2":
            self.order=2
            want_cheese = input ("want a cheese? if Yes write \"Y\" if No write \"N\"  \n ")
            if want_cheese.lower() == "y":
              #self.dic_copy1["meet_burger"]["cheese"] = True
              self.dic_copy1["cheese"] = True

            elif want_cheese.lower() == "n":
              #self.dic_copy1["meet_burger"]["cheese"] = False
              self.dic_copy1["cheese"] = False


            want_lettuce = input ("want a lettuce? if Yes write \"Y\" if No write \"N\" \n ")
            if want_lettuce.lower()  == "y":
             #self.dic_copy1["meet_burger"]["lettuce"] = True
             self.dic_copy1["lettuce"] = True

            elif want_lettuce.lower() == "n":
              #self.dic_copy1["meet_burger"]["lettuce"] = False
              self.dic_copy1["lettuce"] = False


            want_mayonnaise=input("want a mayonnaise? if Yes write \"Y\" if No write \"N\" \n")
            if want_mayonnaise.lower()  == "y":
             # self.dic_copy1["meet_burger"]["mayonnaise"] = True
              self.dic_copy1["mayonnaise"] = True

            elif want_mayonnaise.lower() == "n":
             # self.dic_copy1["meet_burger"]["mayonnaise"] = False
              self.dic_copy1["mayonnaise"] = False


            want_meal =input("want a meal? if Yes write \"Y\" if No write \"N\" \n")
            if want_meal.lower()  == "y":
              #self.dic_copy1["meet_burger"]["meal"] = True
              self.dic_copy1["meal"] = True
              return self.dic_copy1.items() , "Your price is 25.RS :) "


            elif want_meal.lower() == "n":
              #self.dic_copy1["meet_burger"]["meal"] = False
              self.dic_copy1["meal"] = False
              return self.dic_copy1.items() , "Your price is 15.RS :) "
    
        else:
          raise Exception(Fore.RED + "\n Try again with a valid option please :(  \n")
          
      
      
    def display(self, request):
      '''this funcaion display the details of the order'''


      if request == "3":

          
          if self.order==1:
            return list(self.dic_copy.items()) 
          
                
        
          
          if self.order==2:
            return list(self.dic_copy1.items()) 
          
          else:
            raise Exception(Fore.RED + "Please order somthing")
      
     


      

       



    

    

