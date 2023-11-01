from colorama import Fore , Style , Back
from art import *



from CalorisCalculator import CalorieCalculator 
nutrition_data = {
    'rice': {'Calories': 130, 'protein': 2.7, 'fat': 0.3, 'carbohydrates': 28.7},
    'chicken': {'Calories': 335, 'protein': 25.6, 'fat': 3.6, 'carbohydrates': 0.0},
    'vegetables': {'Calories': 35, 'protein': 1.2, 'fat': 0.2, 'carbohydrates': 7.6},
    'meat': {'Calories': 216, 'protein': 20, 'fat': 15, 'carbohydrates': 0.0},
    'egg': {'Calories': 143, 'protein': 12.57, 'fat': 9.94, 'carbohydrates': 0.78}
}

print(Fore.YELLOW, "Welcome to our Calories Calculator!")
tprint("**Calories Calculator**")
print(Style.RESET_ALL)
calorie_calculator = CalorieCalculator(nutrition_data)

while True:
    component = input("Enter the meal type (type 'done' to exit): ")
    component = component.lower()
    if component == 'done':
        break
    try:
        quantity = float(input("Enter the quantity (in grams): "))
        calorie_calculator.add_component(component, quantity)
        if component not in nutrition_data:
            calorie_calculator.add_nutrition(component)
        total_calories = calorie_calculator.calculate_calories()

        high_calorie_threshold = 500
        color = Fore.RED if total_calories > high_calorie_threshold else Fore.GREEN
        colored_calories = color + str(total_calories) + Style.RESET_ALL

        print("Total calories for the meal are:", colored_calories, "calories")
        with open('file.txt', 'a') as file:
            file.write(
                f"Meal: {component}, Quantity: {quantity}g, Total Calories: {total_calories} calories\n"
            )

    except ValueError:
        print("Error: Please enter a valid numeric value for quantity.")
    except ZeroDivisionError:
        print("Error: There is no nutritional data for the components.")

print(Fore.BLUE, "Thank you for using the Calories Calculator program. Come back again soon.")
print(Style.RESET_ALL)



