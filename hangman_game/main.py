from functions import hangman
from art import *
from colorama import *
from tabulate import *

game = hangman()

print(Back.WHITE+Fore.BLACK+Style.BRIGHT+text2art('WELCOME TO HANGMAN',font="basic"))
game.add_word("dog")
game.list_words()

while False: 
    print('''
1.
2.
3.
4.
5.       
          ''')