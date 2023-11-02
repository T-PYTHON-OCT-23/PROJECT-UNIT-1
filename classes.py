from clint import Clint
import json
from prettytable import PrettyTable
from prettytable import from_json
from colorama import Fore, Back, Style,init
import hashlib
init(autoreset=True)


x = PrettyTable()
clints= []

try:
    with open("clint.json", "r", encoding="utf-8") as file:
        content = file.read()
        clints = json.loads(content)
except:
    pass

def sing_in() :
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    password = input("Enter your password : ")
    
    for n in range(0 , len(clints)):
        if str(email) ==  str(json.dumps(clints[n]["email"])):
            return print("Your email address is already registered, just log in") 
    
    try:
        add_clint = Clint(name,email,password)
        add_clint.set_name(name)
        add_clint.set_email(email)
        add_clint.set_password(password)
        
        clint ={
            "name":add_clint.get_name(),
            "email":add_clint.get_email(),
            "password":add_clint.get_password(),
            "points": 0
        }
    except Exception as e:
        print(e)
    clints.append(clint)
    
    with open("clint.json", "w", encoding="utf-8") as file:
        content = json.dumps(clints)
        file.write(content)
    print(Fore.GREEN +"\nYou are successfully registered, just log in")
    


def log_in():
    email = input("Enter your email : ")
    password = input("Enter your password : ")
    for n in range(0 , len(clints)):
        if email ==  (clints[n]["email"]) and password ==  (clints[n]["password"]):
            print(Fore.GREEN +"\nYou have been logged in successfully ")
            return email
    raise Exception(Fore.RED +"The email or password is incorrect , please log in if you do not already have an account")


plant_info=[]
try:
    with open("plants.json", "r", encoding="utf-8") as file:
        content = file.read()
        plant_info = json.loads(content)
except:
    pass

def recording_plant_info(email = None):
    plant_name= input("Enter the name of the plant: ")
    choice1 = """
    Choose the plant variety (choose a number):
    1 - Vascular plant
    2 - Non-vascular plant
    3 - Seed plant
    4 - Angiosperms
    5 - Gymnosperms
    """
    
    classification_of_plant = input(choice1)
    if  not classification_of_plant.isnumeric() :
        raise Exception(Fore.RED +"please choose a number : ") 
    
    
        
    elif classification_of_plant not in ["1" ,"2" ,"3" ,"4", "5"]:
        raise Exception(Fore.RED +"Please enter one of the numbers provided")
    
    elif classification_of_plant == "1" :
        classification_of_plant= "Vascular plant"
    elif classification_of_plant == "2" :
        classification_of_plant= "Non-vascular plant"
    elif classification_of_plant == "3" :
        classification_of_plant= "Seed plant"
    elif classification_of_plant == "4" :
        classification_of_plant= "Angiosperms"
    elif classification_of_plant == "5" :
        classification_of_plant= "Gymnosperms"
    
        
    
    choice2= """
    Choose the type of plant (choose a number):
    1 - Herbs
    2 - Bushes
    3 - The trees
    4 - Reptiles
    5 - The climber
    """
    plant_type = input(choice2)
    if not plant_type.isnumeric() :
        raise Exception(Fore.RED +"please choose a number ") 
        
    elif  plant_type not in ["1" ,"2" ,"3" ,"4", "5"]:
        raise Exception(Fore.RED +"Please enter one of the numbers provided")
    elif plant_type == "1" :
        plant_type= "Herbs"
    elif plant_type == "2" :
        plant_type= "Bushes"
    elif plant_type == "3" :
        plant_type= "The trees"
    elif plant_type == "4" :
        plant_type= "Reptiles"
    elif plant_type == "5" :
        plant_type= "The climber"
        
        
        
    choice3 = """
    Reproduction method (choose a number):
    1 - Sexual reproduction
    2 - Asexual reproduction
    """
    reproduction_method = input(choice3)
    if not reproduction_method.isnumeric() :
        raise Exception(Fore.RED +"please choose a number ") 
        
    elif  reproduction_method not in ["1" ,"2"]:
        raise Exception(Fore.RED +"Please enter one of the numbers provided")
    elif reproduction_method == "1" :
        reproduction_method= "Sexual reproduction"
    elif reproduction_method == "2" :
        reproduction_method= "Asexual reproduction"
        
    general_info = input("Enter what you know about the plant : ")
    
    plant = {
        "plant name":plant_name,
        "classification of plant": classification_of_plant,
        "plant type":plant_type,
        "reproduction method":reproduction_method,
        "general info" : general_info
    }
    
    plant_info.append(plant)
    for n in range(0 , len(clints)):
        if clints[n]["email"] == email  :
            clints[n]["points"] = clints[n]["points"] +1
    
    print(Fore.GREEN +"\nThank you, the information has been added successfully")
    input(Fore.LIGHTBLACK_EX +"--- Press any key to continue ---")
    print(Style.RESET_ALL)

    with open("plants.json", "w", encoding="utf-8") as file:
        content = json.dumps(plant_info)
        file.write(content)
    with open("clint.json", "w", encoding="utf-8") as file:
        content = json.dumps(clints)
        file.write(content)  

def display_plants():
    with open("plants.json") as fp:
        mytable = from_json(fp.read())
        t = mytable.get_string()
        print(t)
    input(Fore.LIGHTBLACK_EX +"--- Press any key to continue ---")
    print(Style.RESET_ALL)
        
        
problems_faced = []
try:
    with open("problems_faced.json", "r", encoding="utf-8") as file:
        content = file.read()
        problems_faced = json.loads(content)
except:
    pass

plant_problems = []
def problem_faced():
    plant_name= input("Enter the name of the plant: ")
    choice1 = """
    Choose the plant variety (choose a number):
    1 - Vascular plant
    2 - Non-vascular plant
    3 - Seed plant
    4 - Angiosperms
    5 - Gymnosperms
    """
    classification_of_plant = input(choice1)
    if not classification_of_plant.isnumeric() :
        raise Exception(Fore.RED +"please choose a number ") 
        
    elif  classification_of_plant not in ["1" ,"2" ,"3" ,"4", "5"]:
        raise Exception(Fore.RED +"Please enter one of the numbers provided")
    
    elif classification_of_plant == "1" :
        classification_of_plant= "Vascular plant"
    elif classification_of_plant == "2" :
        classification_of_plant= "Non-vascular plant"
    elif classification_of_plant == "3" :
        classification_of_plant= "Seed plant"
    elif classification_of_plant == "4" :
        classification_of_plant= "Angiosperms"
    elif classification_of_plant == "5" :
        classification_of_plant= "Gymnosperms"
    
        
    
    choice2= """
    Choose the type of plant (choose a number):
    1 - Herbs
    2 - Bushes
    3 - The trees
    4 - Reptiles
    5 - The climber
    """
    plant_type = input(choice2)
    if not plant_type.isnumeric() :
        raise Exception(Fore.RED +"please choose a number ") 
        
    elif  plant_type not in ["1" ,"2" ,"3" ,"4", "5"]:
        raise Exception(Fore.RED +"Please enter one of the numbers provided")
    elif plant_type == "1" :
        plant_type= "Herbs"
    elif plant_type == "2" :
        plant_type= "Bushes"
    elif plant_type == "3" :
        plant_type= "The trees"
    elif plant_type == "4" :
        plant_type= "Reptiles"
    elif plant_type == "5" :
        plant_type= "The climber"
        
        
        
    choice3 = """
    Reproduction method (choose a number):
    1 - Sexual reproduction
    2 - Asexual reproduction
    """
    reproduction_method = input(choice3)
    if not reproduction_method.isnumeric() :
        raise Exception(Fore.RED +"please choose a number ") 
        
    elif reproduction_method not in ["1" ,"2"]:
        raise Exception(Fore.RED +"Please enter one of the numbers provided")
    elif reproduction_method == "1" :
        reproduction_method= "Sexual reproduction"
    elif reproduction_method == "2" :
        reproduction_method= "Asexual reproduction"
        
    the_problem = input("What problem did you encounter? : ")
    
    plant_problem = {
        "number of problem":problems_faced[-1]["number of problem"]+1 ,
        "plant name":plant_name,
        "classification of plant": classification_of_plant,
        "plant type":plant_type,
        "reproduction method":reproduction_method,
        "the problem" : the_problem,
        "A proposal to solve the problem": " "
    }
    
    problems_faced.append(plant_problem)
    print(Fore.GREEN +"Thank you, your problem was successfully solved")
    input(Fore.LIGHTBLACK_EX +"--- Press any key to continue ---")
    print(Style.RESET_ALL)

    with open("problems_faced.json", "w", encoding="utf-8") as file:
        content = json.dumps(problems_faced)
        file.write(content)
        

     
def solve_problem(email = None):
    print("The problems")
    with open("problems_faced.json") as fp:
        mytable = from_json(fp.read())
        t = mytable.get_string()
        print(t)
        
    num_of_problem = int(input("Enter number of problem: "))
    if not type(num_of_problem) is int:
        raise Exception(Fore.RED +"please choose a number of problem ")
    
        
    for n in range(0 , len(problems_faced)):
        if n == len(problems_faced):
            print(f"Sorry, problem number {num_of_problem} does not exist ")
        if problems_faced[n]["number of problem"] == num_of_problem:
            suggested_solution = input("Suggest a solution to this problem : ")
            problems_faced[n]["A proposal to solve the problem"] = suggested_solution
            with open("problems_faced.json", "w", encoding="utf-8") as file:
                content = json.dumps(problems_faced)
                file.write(content)
            break
    for n in range(0 , len(clints)):
        if clints[n]["email"] == email  :
            clints[n]["points"] = clints[n]["points"] +2
            
    with open("clint.json", "w", encoding="utf-8") as file:
        content = json.dumps(clints)
        file.write(content)
    print(Fore.GREEN +"Thank you, your suggestion has been added to solve the problem successfully")
    input(Fore.LIGHTBLACK_EX +"--- Press any key to continue ---")
    print(Style.RESET_ALL)



def show_registered_users(email = None):
    if email != "oudy@gmail.com":
        return print(Fore.RED +"Sorry, only Admin can see this information\n") , input(Fore.LIGHTBLACK_EX +"--- Press any key to continue ---") ,print(Style.RESET_ALL)
    with open("clint.json") as fp:
        mytable = from_json(fp.read())
        t = mytable.get_string()
        print(t)
        
    not_interacting = list(filter(lambda clint: clint["points"] == 0, clints ))
    print("Non-interactive members : ")
    for n in range(1,len(not_interacting)):
        if n == len(not_interacting)-1 :
            print(not_interacting[n]["name"])
            break
        print(not_interacting[n]["name"] , end=" , ")


    input(Fore.LIGHTBLACK_EX +"--- Press any key to continue ---")
    print(Style.RESET_ALL)



#print(hashlib.md5(add_clint.get_email().encode()))


    