from art import *
from colorama import *
from movie import *
from snak import *
from termcolor import *

print(Fore.MAGENTA)
tprint("CinemaX", space=10)
print(Style.RESET_ALL)
tprint("Welcome  To  CinemaX")
print(Style.RESET_ALL)
cprint("Here are the available movies:", "light_magenta", "on_white")
print(Style.RESET_ALL)
print(Fore.MAGENTA)
display_movies()
print(Style.RESET_ALL)
print(Fore.MAGENTA)

while True:
    movie_choice:int = input("Please enter the number of the movie you want to watch: ")
    if movie_choice.isdigit() and int(movie_choice) in range(1, len(movies) + 1):
        movie_choice = int(movie_choice)
        break
    else:
        cprint("Invalid input. Please try again 😢.","red","on_red")

selected_movie = movies[movie_choice - 1]
print(Style.RESET_ALL)
# ------------------------------------حجز المقعد-----------------------------------

hall_seats = {"1": ["A1", "A2", "A3", "B1", "B2", "B3"],
              "2": ["C1", "C2", "C3", "D1", "D2", "D3"],
              "3": ["E1", "E2", "E3", "F1", "F2", "F3"],
              "4": ["A1", "A2", "A3", "B1", "B2", "B3"],
              "5": ["E1", "E2", "E3", "F1", "F2", "F3"]}

while True:
    cprint(f"You have selected {selected_movie.name_movie} at {selected_movie.time} in Hall {selected_movie.hall}.", "light_magenta", "on_white")
    print("                          ")
    for seat in hall_seats[str(selected_movie.hall)]:
        print(f"Seat {seat} is available.")
    print("                          ")   
    seat_choice = str(input("Please enter the seat number you want: ")).upper()
    if seat_choice in hall_seats[str(selected_movie.hall)]:
        break
    else:
        print("Invalid seat number. Please try again.😢","red","on_red")

#--------------------------------------- سناك --------------------------------------

snacks = [snack1, snack2,snack3]
snacks_order = []


while True:

    try:
        cprint( "do you want snaks?","light_magenta")
        for i, snack in enumerate(snacks):
            print(f"{i+1}. {snack.name} - {snack.price} $")

        snack_choice = input("Do you want to order a snack? or enter: ")
        if not snack_choice:
            break
        snack = snacks[int(snack_choice) - 1]
        snacks_order.append(snack)

        print("Your order :")
        for snack in snacks_order:
            print(f"{snack.name} - {snack.price} $ ")
    except Exception as e:
        print(e) 


# --------------------------------------------------------------------------------

total_price = selected_movie.price + sum(snack.price for snack in snacks_order)
cprint(f"Total : {total_price} $","light_magenta")
#-------------------------------------------------------------------------

x=34543  #ارقام عشوائية عشان رقم التكت بس
y=234
z=12
ticket_number= lambda x,y,z :x+y+z+1
#---------------------------------تاكيد الطلب ------------------------------------- 

while True:
    confirm_order = input("Do you want to confirm your order? (yes/no) ")
    if confirm_order.lower() == "yes":
        cprint("Your order has been confirmed!✅","light_magenta","on_white")
        break
    elif confirm_order.lower() == "no":
        cprint("Your order has been cancelled.😢","red","on_red")
        break
    else:
        cprint("Invalid input. Please try again.🤨","red","on_red")

print(" ")
#--------------------------------طباعة التذكرة --------------------------------- 

if confirm_order.lower() == "yes":
    cprint("* Please make payment and collect your ticket 🩷 ","light_magenta","on_white")
    cprint("-"*50, "light_magenta")
    cprint("CinemaX", "light_magenta")
    cprint("-"*50, "light_magenta")
    cprint(f"Movie: {selected_movie.name_movie}", "light_magenta")
    cprint(f"Time: {selected_movie.time}", "light_magenta")
    cprint(f"Hall: {selected_movie.hall}", "light_magenta")
    cprint(f"Seat: {seat_choice}", "light_magenta")
    cprint("-"*50, "light_magenta")
    cprint("Your order :", "light_magenta")
    for snack in snacks_order:
      cprint(f"{snack.name} - {snack.price} $ ", "light_magenta")
    cprint(f"Movie - {selected_movie.price} $", "light_magenta")
    cprint(f"Total : {total_price} $", "light_magenta")
    cprint("-"*50, "light_magenta")
    cprint(f"Ticket Number: {ticket_number(x,y,z)+1}", "light_magenta")
    cprint("-"*50, "light_magenta")
    tprint("Thank  You 🤍!")

