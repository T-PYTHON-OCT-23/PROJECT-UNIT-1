import classes
from art import *
from colorama import Fore, Back, Style,init
init(autoreset=True)

the_list = """
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        ~!~ Date/Time example of py_menu ~!~
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Choose what you want from the following options by entering the number :
1 ) Adding parameters for a specific plant .
2 ) View information about registered plants .
3 ) Ask a problem you encountered with one of the plants .
4 ) See the problems faced by a lighting fixture and suggest a solution. 
5 ) View registered members and their points.
6 ) To go out.
Choose a number :  """
Art=text2art("           Welcome   to \nthe   plant   community")
print(Style.DIM+Art)
while True:
    
    choice = input(the_list)
    try:
        if not choice.isnumeric() :
            raise print("Please enter the number of one of the available options")
        if int(choice) == 1:
            classes.recording_plant_info()
        elif int(choice) == 2 :
            classes.display_plants()
        elif int(choice) == 3 :
            classes.problem_faced()
        elif int(choice) == 4:
            classes.solve_problem()
        elif int(choice) == 5 :
            classes.show_registered_users()
        elif int(choice) == 6:
            tprint("    Thanks   for   visiting  \n    see    you   later.")
            break
        else:
            print(Fore.RED +f"No results found for {choice} ")
            print("Please enter the number of one of the available options")
    except Exception as e:
        print(e)

    
        
        