
from colorama import Fore, Style
from art import *


class CalorieCalculator:
    def __init__(self, nutrition_data):
        self.nutrition_data = nutrition_data
        self.meal = {}

    def add_component(self, component, quantity):
        self.meal[component] = quantity

    def add_nutrition(self, component):
        if component not in self.nutrition_data:
            print("This meal is not in the nutrition data. Do you want to add a new component?")
            answer = input("Enter 'yes' to add or 'no' to skip: ")
            if answer.lower() == "yes":
                calories = float(input("Enter the calories per 100g: "))
                protein = float(input("Enter the protein per 100g: "))
                fat = float(input("Enter the fat per 100g: "))
                carbohydrates = float(input("Enter the carbohydrates per 100g: "))
                self.nutrition_data[component] = {
                    'Calories': calories,
                    'protein': protein,
                    'fat': fat,
                    'carbohydrates': carbohydrates
                }
                print(f"{component} has been added to the nutrition data.")
            else:
                print(f"{component} has been skipped.")

    def calculate_calories(self):
        total_calories = 0
        for component, quantity in self.meal.items():
            if component in self.nutrition_data:
                calories_per_100g = self.nutrition_data[component]['Calories']
                total_calories += (calories_per_100g / 100) * quantity
        return total_calories


