import random
import re
import colorama
from colorama import Fore, Back, Style
from SoundEffects import play_correct_answer_sound, play_incorrect_answer_sound, play_yay_sound
    
#Class of escape room 
class EscapeRoom:
    def __init__(self, story, puzzles):
        #Attribute
        self.story = story
        self.puzzles = puzzles
        try:
            self.current_puzzle = random.choice(puzzles) 
        except IndexError:
            print("You can not play on the same room after you registered.\n Press on Enter to Exit")
            input()

    def play(self):
        print(self.story)
        try:
            print(self.current_puzzle.get_puzzle())
        except Exception as e:
            print(e)

        answer = input("Answer: ")
        if self.current_puzzle.check_answer(answer):
            correct = colorama.Fore.GREEN + colorama.Style.BRIGHT + "Correct!" + colorama.Style.RESET_ALL
            print(correct)
            play_correct_answer_sound()
            self.puzzles.remove(self.current_puzzle)
            if len(self.puzzles) == 0:
                print(Fore.CYAN)
                #play_yay_sound()
                you_escaped= " You escaped! "
                print(you_escaped)
                print("Congrats on completing all the questions!")
                print(colorama.Style.RESET_ALL)
                return True

            self.current_puzzle = random.choice(self.puzzles)
        else:
            incorrect= colorama.Fore.RED + "Incorrect." + colorama.Style.RESET_ALL
            print(incorrect)
            #play_incorrect_answer_sound()

        return False

#Class of Puzzle 
class Puzzle:
    def __init__(self, puzzle, answer):
        self.puzzle = puzzle
        self.answer = answer

    def get_puzzle(self):
        return self.puzzle

    def check_answer(self, answer):
        list_correct_answer.append(answer)
        return self.answer == answer

#the 4 different stories
room1 = "You are trapped in a queen of hearts castle. You must solve the puzzles to escape before the queen get you!"
room2 = "You are lost in a maze. You must solve the puzzles to find your way out!"
room3 = "You are trapped in a killer house. You must solve the puzzles to escape before the killer comes back!"
room4 = "You are trapped in a spaceship that is crashing towards the sun. You must solve the puzzles to fix the ship and escape before it's too late!"


#Stories
room1_puzzles = [
    Puzzle("You are now in a room that is filled with money.\nWhat has a head and a tail but nobody?", "Coin"),
    Puzzle("Now you are in the Library room.\nWhat building has the most stories?", "Library"),
    Puzzle("Now you are in the kitchen.\nWhat would you eat? Becarful candy is dangrous(Cake - Biscuit - Cheesecake- Cupcake)", "Biscuit"),
    Puzzle("Now you are in the garden.\nWatch out,the rains fall down.\n What goes up when rain comes down?","Umbrella")
]

room2_puzzles = [
    Puzzle("What has a neck without a head, two arms without hands, and a belly without a bottom?\nyou can waer it", "Shirt"),
    Puzzle("What has two hands but no arms or legs?\nYou can see the time from it", "Clock"),
    Puzzle("What is at the end of a rainbow?", "W"),
]

room3_puzzles = [
    Puzzle("A calender found in ground that contains [1 , 4 , 9 , 10 , 11].\nTry to find name of the killer?", "Jason"),
    Puzzle("What is sharp, but can't cut itself?", "Knife"),
    Puzzle("I have four fingers and a thumb, but not alive?\nThe Killer tries to hide his fingerprint", "Glove"),
]

room4_puzzles = [
    Puzzle("People buy me to eat but never eat me?\nYou put the food on it", "Plate"),
    Puzzle("I go around and in the house but never touches the house. What am I?\n You can see it only in the morning","Sun"),
    Puzzle("What is the name of the most famous space exploration agency?", "NASA"),
]


#list of all the rooms
rooms = [room1, room2, room3, room4]

#list of all the puzzles
puzzles = [room1_puzzles, room2_puzzles, room3_puzzles, room4_puzzles]

#Empty dictionary
participants = {}
#Empty list
list_correct_answer =[]

#Function to append after choosing 
def choose_same_puzzle_without_removing(puzzles):
  chosen_puzzles = []
  copy_of_puzzles = puzzles.copy()

  while copy_of_puzzles:
    puzzle = random.choice(copy_of_puzzles)
    chosen_puzzles.append(puzzle)
    copy_of_puzzles.remove(puzzle)

  return chosen_puzzles

#Function to calculate the total correct answers 
def total_answers(list_correct_answer:int)->int:

    value = lambda length_list: (13 - length_list)
    total_answers = value(len(list_correct_answer))
    return total_answers


#Start the game
def start_the_program():
    print(Fore.CYAN)
    print("Choose a Room:")
    for i in range(len(rooms)):
        print(f"{i + 1}. {rooms[i]}")
    try:
        user_choice = int(input("Enter the room you want to join: ")) 
    except ValueError:
        print("\033[31mEnter only from the menu that appears to you.\033[0m")
        start_the_program()
        
    #Create an escape room object for the chosen story
    room_index = user_choice - 1
    try:
        escape_room = EscapeRoom(rooms[room_index], puzzles[room_index])
    except IndexError:
        print("list index out of range")

    print(colorama.Style.RESET_ALL)

    # Play the game
    try:
        while not escape_room.play():
            pass
    except Exception as e:
        print(e)

#if player want to play again or to exit. 
def display_the_menu():
    while True:
        print("Do you want to play again?")
        user_choice = input("-Type \033[34m1\033[0m for Yes\n-Type \033[36m2\033[0m Display information about Q&A\n-Type \033[35m3\033[0m for exit\n Choose an option:")
        if user_choice == '1':
            start_the_program()
        elif user_choice == "2":
            print(f"Answers: {list_correct_answer}")
            value_total_answers = total_answers(list_correct_answer)
            print(f"Questions letf:{value_total_answers}.")
            print(f"Questions you got it right:{value_total_answers-len(list_correct_answer)}.")
        elif user_choice =='3':
            print("\033[35mThank you for your time see you soon!\033[0m")
            break
        else:
            print("Invaild input, please try again.")

