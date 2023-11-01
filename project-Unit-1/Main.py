from colorama import Fore , Style , Back
from art import *



from CalorisCalculator import CalorieCalculator 


nutrition_data =  {
                  'rice':{ 'Calories':130 ,'proten':2.7,'fat':0.3,'carbohydrates':28.7},
                  'chicken':{'Calories':335 ,'proten':25.6,'fat':3.6,'carbohydrates':0.0},
                  'vegetables':{'Calories':35,'proten':1.2,'fat':0.2,'carbohydrates':7.6},
                  'meat':{'Calories':216,'proten':20,'fat':15,'carbohydrates':0.0} ,
                  'egg':{'Calories':143,'proten':12.57,'fat':9.94,'carbohydrates':0.78}
                      }


   
print(Fore.YELLOW,"Welcome to our calories Calculator!")
tprint("**calories")
tprint("calculator **") 
print(Style.RESET_ALL)
calorie_calculator = CalorieCalculator(nutrition_data)

while True:
        component = input("Enter the meal type ,(type 'done' to exit): ")
        component = component.lower()
        if component == 'done':
            break
        try:
            quantity = float(input("Enter the quantity (in grams): "))
            calorie_calculator.add_component(component, quantity)
            total_calories = calorie_calculator.calculate_calories()

            high_calorie_threshold = 500
            color = Fore.RED if total_calories > high_calorie_threshold else Fore.GREEN
            colored_calories = color + str(total_calories) + Style.RESET_ALL

            print("Total calories for the meal are:", colored_calories, "calories")
            with open('file.txt', 'a') as file:
                    file.write(
                    f"Total Calories: {total_calories} calories\n"
                    )

        except ValueError:
            print("Error: Please enter a valid numeric value for quantity.")
        except ZeroDivisionError:
                print("Error: There is no nutritional data for the components.")

        except Exception as e:
              print(e)

print(Fore.BLUE,"Thank you for using the Calorie Calculator program. Come back again soon.")
print(Style.RESET_ALL)


