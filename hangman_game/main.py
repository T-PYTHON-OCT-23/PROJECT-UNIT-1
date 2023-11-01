from functions import hangman
from art import *
from colorama import *
from tabulate import *

game = hangman()
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+text2art('WELCOME TO HANGMAN',font='basic'))
intro=  [
["1","START THE GAME"],
["2","LEADERBOARD"],
["3","WORD LIST (cheat code)"],
["4","ADD A WORD TO THE LIST"],
["5","EXIT"]
         ]
try:
    while True:
        print(tabulate(intro,headers=["#","Please choose an option to proceed"],tablefmt="grid"))
        option=input("must be a number from 1-5: ")
        if option=="1":
            game.play()
            input("press any key to proceed")
        elif option=="2":
            game.leaderboard_print()
            input("press any key to proceed")
        elif option=="3":
            game.list_words()
            input("press any key to proceed")
        elif option=="4":
            word=input("Enter a word: ")
            game.append_word(word)
        elif option=="5":
            print("Good bye !"+Style.RESET_ALL)
            break
        else:
            input("Not valid input !")
            
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except EncodingWarning as e:
    print(e)
except Exception as e:
    print(e)