import random
from art import *
import colorama
from colorama import Fore, Back, Style
import playsound

#Class of escape room 
class EscapeRoom:
    def __init__(self, story, puzzles):
        #Attribute
        self.story = story
        self.puzzles = puzzles
        try:
            self.current_puzzle = random.choice(puzzles) 
        except IndexError:
            print("You can not play on the same room after you escaped.\n Press on Enter to Exit")
            start_the_program()
        except UnboundLocalError:
            pass
            input()

    def play(self):
        print(self.story)
        try:
            print(f"Q-{self.current_puzzle.get_puzzle()}")
        except Exception as e:
            print(e)
            input()

        answer = input("Answer: ")
        if self.current_puzzle.check_answer(answer):
            correct = colorama.Fore.GREEN + colorama.Style.BRIGHT + "Correct!" + colorama.Style.RESET_ALL 
            print(correct)
            playsound.playsound("correct_answer.wav")
            self.puzzles.remove(self.current_puzzle)
            if len(self.puzzles) == 0:
                print(Fore.CYAN)
                you_escaped= " You escaped! "
                playsound.playsound("yay_sound.wav")
                tprint(you_escaped,font='sub zero')
                print("Congrats you escaped!")
                print(colorama.Style.RESET_ALL)
                return True

            self.current_puzzle = random.choice(self.puzzles)
        else:
            incorrect= colorama.Fore.RED + "Incorrect." + colorama.Style.RESET_ALL
            print(incorrect)
            playsound.playsound("incorrect_answer.wav")

        return False

#Class of Puzzle 
class Puzzle:
    def __init__(self, puzzle, answer):
        self.puzzle = puzzle
        self.answer = answer

    def get_puzzle(self):
        return self.puzzle

    def check_answer(self, answer):
        if self.answer == answer:
            list_answers.append(answer)
        return self.answer == answer

#the 4 different stories
room1 = "You are trapped in a queen of hearts castle. You must solve the puzzles to escape before the queen get you!"
room2 = "You are lost in a maze. You must solve the puzzles to find your way out!"
room3 = "You are trapped in a killer house. You must solve the puzzles to escape before the killer comes back!"
room4 = "You are trapped in a spaceship that is crashing towards the sun. You must solve the puzzles to fix the ship and escape before it's too late!"


#Stories
room1_puzzles = [
    Puzzle("\033[35mYou are now in a room that is filled with money.What has a head and a tail but nobody?\033[0m\nHint: Something in the room", "Coin"),
    Puzzle("\033[35mNow you are in the Library room.What building has the most stories?\033[0m\nHint:You are in the building..", "Library"),
    Puzzle("\033[35mNow you are in the kitchen. What would you eat? \033[0m\nHint:Be careful \033[31mC\033[0mandy is dangrous(Cake - Biscuit - Cheesecake- Cupcake)", "Biscuit"),
    Puzzle("\033[35mNow you are in the garden. What goes up when rain comes down?\033[0m\nHint: Watch out,the rains fall down.","Umbrella")
]

room2_puzzles = [
    Puzzle("\033[34mWhat has a neck without a head, two arms without hands, and a belly without a bottom?\033[0m\nHint: You can waer it", "Shirt"),
    Puzzle("\033[34mWhat has two hands but no arms or legs?\033[0m\nHint: You can see the time from it", "Clock"),
    Puzzle("\033[34mWhat is at the end of a rainbow?\033[0m\nHint: Read rainboW again..", "W"),
]

room3_puzzles = [
    Puzzle("\033[31mA calender found in ground that contains [1 , 4 , 9 , 10 , 11].\033[0m\nHint:Try to find name of the killer?", "Jason"),
    Puzzle("\033[31mWhat is sharp, but can't cut itself?\033[0m\nHint:You can use it to cut fruits", "Knife"),
    Puzzle("\033[31mI have four fingers and a thumb, but not alive?\033[0m\nHint:The Killer tries to hide his fingerprint", "Glove"),
]

room4_puzzles = [
    Puzzle("\033[33mWhat is the value of 101110 ?\033[0m\nHint: Crack the code", "46"),
    Puzzle("\033[33mI go around and in the house but never touches the house. What am I?\033[0m\nHint : You can see it only in the morning","Sun"),
    Puzzle("\033[33mWhat is the name of the most famous space exploration agency?\033[0m\nHint:Start with letter N.", "NASA"),
]


#list of all the rooms
rooms = [room1, room2, room3, room4]

#list of all the puzzles
puzzles = [room1_puzzles, room2_puzzles, room3_puzzles, room4_puzzles]

#Empty dictionary
participants = {}
#Empty list
list_answers =[]

#function to get the length of list of correct answers
def list_len_answers(list_answers:int)->int:
    value = lambda length_list: (length_list)
    total_answers = value(len(list_answers))
    return total_answers


#Function to start the game
def start_the_program():
    print(Fore.CYAN)
    print("Choose a Room:")
    for i in range(len(rooms)):
        print(f"{i + 1}. {rooms[i]}")
    try:
        room_index = int(input("Enter the room you want to join: "))-1
    except ValueError:
        print("\033[31mEnter only from the menu that appears to you.\033[0m")
        display_the_menu()
    #Create an escape room object for the chosen story
    try:
        escape_room = EscapeRoom(rooms[room_index], puzzles[room_index])
    except IndexError:
        print("list index out of range")
        start_the_program()
    print(colorama.Style.RESET_ALL)
    try:
        while not escape_room.play():
            pass
    except Exception as e:
        print(e)



#Display menu: play again / display A&Q / exit. 
def display_the_menu():
    while True:
        print("-*-"*30)
        print("Do you want to play again?")
        user_choice = input("-Type \033[34m1\033[0m for Yes\n-Type \033[36m2\033[0m for display information about Q&A\n-Type \033[35m3\033[0m for exit\n Choose an option:")
        if user_choice == '1':
            start_the_program()
        elif user_choice == "2":
            print(Fore.CYAN)
            print(f"Answers: {list_answers}")
            value_total_answers = list_len_answers(list_answers)
            print(f"Questions answered: {value_total_answers}")
            questions_left = 13 - value_total_answers
            if questions_left == 0:
                print("\033[33mYou did a great job on completing all the Escape rooms!\033[0m")
                playsound.playsound("win_sound.wav")
                break
            print(f"Questions left: {questions_left}")
            print("Total questions in all rooms: 13")
            print(colorama.Style.RESET_ALL)

        elif user_choice =='3':
            print("\033[35mThank you for your time see you soon!\033[0m")
            break
        else:
            print("\033[31mInvaild input, please try again.\033[0m")
        


