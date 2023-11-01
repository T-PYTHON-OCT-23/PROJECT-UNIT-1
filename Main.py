from Online_escape_room import start_the_program, display_the_menu
from art import *
from colorama import Fore, Back, Style
import colorama

#Project name
print(Fore.CYAN)
title = text2art("Online Escape Room")
print(title)

#Start to play online escape room
start_the_program()
#Display menu: play again / info A&Q / exit. 
display_the_menu()
