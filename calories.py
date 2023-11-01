from stringcolor import * 

class Info:

    def __init__(self, height:float ,weight:float , age:float , gender:str, activity_level:str  ,bmi:float=0.0 , bmr:float=0.0) -> None:
        self.height= height
        self.weight = weight
        self.age = age
        self.gender = gender
        self.activity_level = activity_level
        self.bmi=bmi
        self.bmr = bmr

    
#function to calculate BMI
    def Bmi_calculater(self, var_bmi): 
        '''this function take bmi from lembda and compare it'''
    
        if (var_bmi < 18.5): 
            result = f"Your body mas is {var_bmi} you are Underweight"
            return result

    
        elif ( var_bmi >= 18.5 and var_bmi < 24.9): 
            result = f"Your body mas is {var_bmi} you are Healthy"
            return result
    
        elif ( var_bmi >= 24.9 and var_bmi < 30): 
            result = f"Your body mas is {var_bmi} you are Overweight" 
            return result
        
        elif ( var_bmi >= 30): 
            result = f"Your body mas is {var_bmi} you are Suffering from Obesity"
            return result
            

# calculate daily calories 
    def calculate_daily_calories(self):
        '''this function calculate overall calories'''


        if self.gender == "m".lower():
                self.bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)

        elif self.gender == "f".lower():
                self.bmr = 447.593 + (9.247* self.weight) + (3.098* self.height) - (4.330 * self.age)

        while True:
            if self.activity_level == "1":  #1. sedentary   
                calories = f"Your daily calories needs is: {round(self.bmr * 1.2 , 2)} calories"
                return calories

            elif self.activity_level == "2":  #2.lightly active
                    calories = f"Your daily calories needs is:{round(self.bmr * 1.375 ,2)} calories"
                    return calories

            elif self.activity_level == "3": # 3.moderately active
                    calories =  f"Your daily calories needs is: {round(self.bmr * 1.55 , 2)} calories"
                    return calories
               
            elif self.activity_level == "4": # 3.very active
                calories = f"Your daily calories needs is: {round(self.bmr * 1.725 ,2)} calories"
                return calories
            
            elif self.activity_level == "5": # 3.extra active
                calories = f"Your daily calories needs is: {round(self.bmr *  1.9) , 2} calories"
                return calories   

        