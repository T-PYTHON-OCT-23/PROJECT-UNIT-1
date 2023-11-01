import json
import random
from drawings import drawings
from words import *
from tabulate import *
class hangman:
    
    def __init__(self):
        pass     
        self.leaderboard=[]
        try:
            with open("leaderboared.json","r",encoding="utf-8") as file:
                self.leaderboard= json.loads(file.read())
        except Exception as e:
            print(e)
        
    def choose_word(self):
        word=random.choice(words)
        return word

    def setup(self):
        self.word = self.choose_word()
        self.guessed = [] 
        for i in range(len(self.word)):
            self.guessed.append("_")
        
        self.wrong_guesses = 0
        self.used_letters = []
    
    def add_to_leaderboard(self,username,score):
        user_score={"username": username, "score":score}
        try:
            self.leaderboard.append(user_score)
            with open("leaderboared.json","w",encoding="utf-8") as file:
                file.write(json.dumps(self.leaderboard))
        except Exception as e:
            print(e)
        
        


    def get_username(self):
        self.username=input("plrase enter your name: ")

    def display_state(self):
        print(drawings[self.wrong_guesses])
        print()
        print(" ".join(self.guessed))
        print()
        print("Used letters:", ", ".join(self.used_letters))

    def check_guess(self, guess):
        if (
            len(guess) != 1
            or not guess.isalpha()
            or guess in self.used_letters
            or guess in self.guessed
        ):
            print("Invalid guess!")
            return

        if guess in self.word:
            print("Correct!")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.guessed[i] = guess
        else:
            self.wrong_guesses += 1
            self.used_letters.append(guess)
            print("Incorrect!")

    def check_won(self):
        if "_" not in self.guessed:
            print(f'You win! The word was "{self.word}"')
            print(drawings[self.wrong_guesses])
            
            return True
    
    def check_game_over(self):
        if "_" not in self.guessed:
            print(f'You win! The word was "{self.word}"')
            print(drawings[self.wrong_guesses])
            return True

        if self.wrong_guesses >= len(drawings) - 1:
            print(f'You lose! The word was "{self.word}"')
            print(drawings[self.wrong_guesses])
            return True
        
    def leaderboard_print(self):
        self.leaderboard=sorted(self.leaderboard, key=lambda x: x['score'], reverse=True)
        leaderboard=[]
        for index, i in enumerate(self.leaderboard):
            leaderboard.append([index+1,i["username"],i["score"]])
        print(tabulate(leaderboard,headers=["Rank","Name","Score"],tablefmt="fancy_grid",numalign="center",stralign="center"))
    
    def add_word(self,word):
        append_word(word)
        
    def list_words():
        print(words)
    
    def play(self):
        self.score=0
        self.setup()
        while True:
            self.display_state()
            guess = input("Guess a letter: ").lower()
            self.check_guess(guess)
            if self.check_won():
                self.score+=1
                self.setup()
                print(f"great, your score is {self.score}! carry on")

            if self.check_game_over():
                print("better luck next time..")
                self.get_username()
                print(self.username,"your score is:",self.score)
                self.add_to_leaderboard(self.username,self.score)
                print("added to the leaderboard")

                break