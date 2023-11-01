from colorama import Fore , Style , Back



class CalorieCalculator :
    def __init__(self, nutrition_data) :
     self.nutrition_data = nutrition_data
     self.meal = {}

    def add_component(self, component, quantity):
        self.meal[component] = quantity
    


    
    #اضيف هنا داله اسمها add nutrition
    #بحيث اذا ادخل المستخدم وجبه غير موجودة اساله هل تريد ادخال مكون جديد واطلب منه ادخال كم السعرات والبروتين والفات والكارب 

    def calculate_calories(self):
        total_calories = 0
        for component, quantity in self.meal.items():
            if component in self.nutrition_data:
                calories_per_100g = self.nutrition_data[component]['Calories']
                total_calories += (calories_per_100g / 100) * quantity
        
        if total_calories == 0:
            raise Exception("Meal Not found")
        return total_calories

