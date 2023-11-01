from classPadel_Court import Padel_Court
from rating import Court_Rating
from colorama import *
from art import *



padel_way=Padel_Court('riyadh',"Padel Way" ,8,True,3)
padel_pro=Padel_Court('riyadh',"Padel Pro", 3,False,3.5)
padel_art=Padel_Court('riyadh',"Padel Art" ,4,True,5)
padel_loop=Padel_Court('abha',"Padel Loop" ,4,True,5)
padel_earth=Padel_Court('abha',"Padel Earth" ,4,True,4.3)
padel_m3=Padel_Court('abha',"Padel M3" ,4,True,5)
padel_yalla=Padel_Court('alkhobar',"Yalla Padel" ,4,True,4)
padel_mercure=Padel_Court('alkhobar',"Padel Mercure" ,4,True,1.5)
padel_tik=Padel_Court('alkhobar',"Tik Padel" ,4,True,3.4)

court_data ={
    "riyadh":[padel_way,padel_pro,padel_art],
    "abha":[padel_loop,padel_earth,padel_m3],
    "alkhobar":[padel_yalla,padel_mercure,padel_tik]
}
tprint("Welcome")
while True:
    print(Fore.WHITE+"Menu : ")
    print(Fore.WHITE+"** CHOSE NUMBER **")
    print(Fore.WHITE+"1- Selict city ")
    print(Fore.WHITE+"2- Search for court ")
    print(Fore.WHITE+"3- Exit ")
    print(Style.RESET_ALL)

    user_choice = input(Fore.BLUE+"choice :")

    if user_choice == "1":
        print(Fore.BLUE+"** Select city ")
        # Display a list of available cities
        cities = court_data.keys()
        for i, city in enumerate(cities):
            print(f"{i}. {city}")
            print(Fore.BLUE+"-"*50)

        # Prompt the user to select a city
        selected_city_index = int(input(Fore.BLUE+"Enter the indix number of the city: "))
        if selected_city_index >= len(cities):
            print("Please choose valid city index")
        else:
            selected_city = list(cities)[selected_city_index]
            # List all courts in the selected city
            matching_courts = Padel_Court.search(court_data, selected_city)
            for court in matching_courts:
                court.court_info()
                print(Fore.BLUE+"-"*50)
            
    elif user_choice =="2":
        print("** Search for court ")
        while True:
          city = input("Enter a city to search: ").lower()

          if city in court_data:
            for i in court_data[city]:
                print(i.name)
                print(Fore.BLUE + "-" * 50)

            for i, item in enumerate(court_data[city]):
                print(f"{i}. {item.name}")
            break  # Exit the loop if a valid city is entered
          else:
             print("City not found. Please enter a valid city.")

        chosen_court = input("Choose a court by entering the index number: ")
        valid_choice = False
        while not valid_choice:
            try:
                if chosen_court.isdigit():
                    chosen_court_index = int(chosen_court)
                    if chosen_court_index >= 0 and chosen_court_index < len(court_data[city]):
                        selected_court = court_data[city][chosen_court_index]
                        print(Fore.BLUE + f"You selected: {selected_court.name}")
                        valid_choice = True
                    else:
                        print("Invalid court index. Please choose a valid index.")
                else:
                    print("Invalid input. Please enter a valid index.")
            except Exception as e:
                print("An error occurred: " + str(e))
            
            if not valid_choice:
                # Prompt the user to enter the index again
                chosen_court = input("Choose a court by entering the index number: ")

        while True:
             print(Fore.BLUE+"** CHOSE NUMBER **")
             print(Fore.BLUE+"1-add rate ")
             print(Fore.BLUE+"2- add commint ")
             print(Fore.BLUE+"3- Exit ")
             user_choice = input(Fore.BLUE+"choice :")
             if user_choice == "1":
              court_rating = Court_Rating()
            # Add a new rating
              new_rating = input(Fore.BLUE+"Enter your rating from 1 -> 5 wher 5 is the best")  # Replace with the actual rating
              #print(f"{new_rating} \n Thank you for your rating")
              try:
                new_rating = float(new_rating)
                if 1 <= new_rating <= 5:
                    print(Fore.WHITE+f"You rated {selected_court.name} with {new_rating}. Thank you for your rating.")
                    court_rating.add_rating(new_rating)
                     # Update the court's rating
                    selected_court.rate = new_rating
                    print(Fore.BLUE+f"The updated rating for {selected_court.name} is now {new_rating}.")
                else:
                  print(Fore.RED+"Invalid rating value. Please enter a value between 1 and 5.")
              except ValueError:
                    print(Fore.RED+"Invalid input. Please enter a valid numeric rating.")
             elif user_choice == "2":
                new_comment = input(Fore.BLUE+"Enter your comment here: ")
                print(Fore.WHITE+f"You commented on {selected_court.name}: {new_comment}. Thank you for your comment.")
                court_rating.add_comment(new_comment)

                filter_condition = lambda court: court.rate >= 4.0
                #filter the courts
                filtered_courts_list = [court for city_courts in court_data.values() for court in city_courts if filter_condition(court)]
                # Print the filtered courts
                if filtered_courts_list:
                    print(Fore.GREEN+"Courts with a rating greater than or equal to 4.0:\n")
                    for court in filtered_courts_list:
                        court.court_info()
                        print(Fore.GREEN + "-" * 50)
                else:
                    print(Fore.BLUE+"No courts found with a rating greater than or equal to 4.0.")

             elif user_choice == "3":
                break
        print(Style.RESET_ALL)
    elif user_choice == "3":
        print(Fore.RED+"Goodbye!")
        break
    else:
        print(Fore.RED+"Please write a valid choice")  