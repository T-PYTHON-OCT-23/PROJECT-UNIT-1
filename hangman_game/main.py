from functions import hangman
from art import *
from colorama import *
from tabulate import *
from words_file import *

game = hangman()
print(Back.WHITE+Fore.BLACK+Style.BRIGHT+text2art('WELCOME TO HANGMAN',font='basic'))
intro=[
["1","START THE GAME"]
,["2","LEADERBOARD"]
,["3","WORD LIST (cheat code)"]
,["4","ADD A WORD TO THE LIST"]
,["5","EXIT"]]

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
        if word in words:
            print("word is already in the list")
        else:
            game.append_word(word)
            input(f"{word} is added to the word list")
    elif option=="5":
        print("Good bye !"+Style.RESET_ALL)
        break
    else:
        input("Not valid input !")
        
        