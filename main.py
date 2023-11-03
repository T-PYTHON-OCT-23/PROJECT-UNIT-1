import classes
from art import *
from colorama import Fore, Back, Style,init
init(autoreset=True)

user_name =""
user_points =0
intro = """
Choose a number :
1 ) For sing in .
2 ) For log in .
"""


while True:
    choice_for_log_in = input(intro)
    try:
        if not choice_for_log_in.isnumeric() :
            raise print("Please enter the number of one of the available options")
        if int(choice_for_log_in) == 1:
            classes.sing_in()
        elif int(choice_for_log_in) == 2 :
            email = classes.log_in()
            for n in range(0 , len(classes.clints)):
                if classes.clints[n]["email"] == email  :
                    user_name = classes.clints[n]["name"]
                    user_points = classes.clints[n]["points"]
            break
        
        elif int(choice_for_log_in) == 3 :
            break
        else:
            print(Fore.RED +f"No results found for {choice_for_log_in} ")
            print("Please enter the number of one of the available options")
    except Exception as e:
        print(e)



the_list = f"""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        ~!~ Welcome {user_name} to   the  plant  community  ~!~
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Choose what you want from the following options by entering the number :
1 ) Add information for a specific plant .
2 ) View information about registered plants .
3 ) Ask a problem you encountered with one of the plants .
4 ) See the problems faced by a lighting fixture and suggest a solution. 
5 ) View registered members and their points.
6 ) To go out.
Choose a number :  """



Welcome=text2art(f"           Welcome   {user_name}\nto the   plant   community")
Thanks=text2art(f"Thanks  for visiting\n   your  points  {user_points}\n    see    you   later.")
print(Style.DIM+Welcome)
while True:
    
    choice = input(the_list)
    try:
        if not choice.isnumeric() :
            raise Exception("Please enter the number of one of the available options")
        if int(choice) == 1:
            classes.recording_plant_info(email)
        elif int(choice) == 2 :
            classes.display_plants()
        elif int(choice) == 3 :
            classes.problem_faced()
        elif int(choice) == 4:
            classes.solve_problem(email)
        elif int(choice) == 5 :
            classes.show_registered_users(email)
        elif int(choice) == 6:
            print(Style.DIM+Thanks)
            break
        else:
            print(Fore.RED +f"No results found for {choice} ")
            print("Please enter the number of one of the available options")
    except Exception as e:
        print(e)

    
        
        