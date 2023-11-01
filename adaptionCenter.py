from art import *
from colorama import Fore, Back, Style
class Pet:
    def __init__(self, name, petType, age, food, picture):
        self.name = name
        self.petType = petType
        self.age = age
        self.food = food
        self.picture = picture

class AdoptionCenter:
    def __init__(self):
        self.availablePets = []

    def listAvailablePets(self):
        '''
        This function sets the index for each pet in the list and calls the display function to display the available pets
        '''
        for i, pet in enumerate(self.availablePets, start=1):
            print(f"{i}.")
            displayPetPicture(pet)

    def adoptPet(self, petIndex):
        '''
        This function takes the index as a parameter from the user to adopt the pet assigned to the index
        '''
        if 1 <= petIndex and petIndex<= len(self.availablePets):
            adoptedPet = self.availablePets.pop(petIndex - 1)
            print(Fore.GREEN,f"You adopted {adoptedPet.name} the {adoptedPet.petType}! He is now your pet.")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED,"Please enter a number from the list")
            print(Style.RESET_ALL)
        
    def addPet(self, pet):
        '''
        This function takes pet as a parameter to adds a new pet to the list
        '''
        self.availablePets.append(pet)

    def feedPet(self, petIndex):
        '''
        This function takes the index as a parameter from the user to feed the pet assigned to the index
        '''
        if 1 <= petIndex and petIndex <= len(self.availablePets):
            adoptedPet= self.availablePets[petIndex]
            print(Fore.GREEN,f"{adoptedPet.name} is full and happy!")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED,"Please enter a number from the list")
            print(Style.RESET_ALL)

def displayPetPicture(pet):
    '''
    This function takes pet as a parameter to displays the pets in the list
    '''
    print(f"Name: {pet.name}, Type: {pet.petType}, Age: {pet.age} years, Food: {pet.food}")
    print(pet.picture)
