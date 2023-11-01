from adaptionCenter import *
from art import *
from colorama import Fore, Style


adoption_center = AdoptionCenter()

pet1 = Pet("Fido", "Dog", 7, "Beef, Beans", r"""
   / \__
  (    @\____
   /         O
  /   (_____/
 /_____/   U
""")

pet2 = Pet("Whiskers", "Cat", 3, "Salmon, Chicken", r"""
   /\_/\  
  ( o.o ) 
   > ^ <
""")

pet3 = Pet("Lily", "Dog", 10, "Beef, Beans", r"""
   / \__
  (    @\____
   /         O
  /   (_____/
 /_____/   U
""")

pet4 = Pet("Loly", "Cat", 6, "Salmon, Chicken", r"""
   /\_/\  
  ( o.o ) 
   > ^ <
""")

adoption_center.addPet(pet1)
adoption_center.addPet(pet2)
adoption_center.addPet(pet3)
adoption_center.addPet(pet4)

wlecomePhrase = text2art("Welcome    to \n world    of    pets")
print(Fore.LIGHTBLUE_EX, wlecomePhrase)
print(Style.RESET_ALL)

while True:
        print("\nPet Adoption Center Menu:")
        print("1- List available pets")
        print("2- List available pets sorted by age")
        print("3- Adopt a pet")
        print("4- Feed a pet")
        print("5- Add a pet to Adoption Center")
        print("6- Exit")

        choice = input("Enter your choice: ")
   
        if choice == "1":

            print("Available Pets:")
            adoption_center.listAvailablePets()

        elif choice == "2":

            newListSortedByAge = sorted(adoption_center.availablePets , key=lambda pet: pet.age)
            for pet in newListSortedByAge:
                print(f"Name: {pet.name}, Type: {pet.petType}, Age: {pet.age} years, Food: {pet.food}")
                print(pet.picture)

        elif choice == "3":

            try:
                petIndex = int(input("Enter the number of the pet to adopt: "))
                adoptedPet = adoption_center.adoptPet(petIndex)
                

            except Exception as e:
                print(Fore.RED ,"Invalid entry, Please try again and enter number from list.")
                print(Style.RESET_ALL)

        elif choice == "4":

            try:
                petIndex = int(input("Enter the number of the pet to feed: "))
                adoption_center.feedPet(petIndex)

            except Exception as e:
               print(Fore.RED,"Invalid entry, Please try again and enter number from list.")
               print(Style.RESET_ALL)
               
        
        elif choice == "5":
           
            name = input("Enter the pet's name: ")
            typePet = input("Enter the type of pet (Cat, Dog): ")
            age = int(input("Enter the pet's age: "))
            food = input("Enter pet food: ")

            for item in adoption_center.availablePets:
              
               if typePet == "cat":
                    image1 = """
                
                            /\_/\  
                           ( o.o ) 
                            > ^ <
                                """
                    print(f"Name: {name}, Type: {typePet}, Age: {age} years, Food: {food}")
                    print(image1)
                    print(Fore.GREEN,f"{name} has been added successfully")
                    print(Style.RESET_ALL)
                    adoption_center.addPet(Pet(name,typePet,age,food, image1))
                    break
               
               elif typePet == "dog":
                     image1 = """
                              / \__
                             (    @\____
                             /         O
                            /   (_____/
                           /_____/   U
                             """
                     print(f"Name: {name}, Type: {typePet}, Age: {age} years, Food: {food}")
                     print(image1)
                     print(Fore.GREEN,f"{name} has been added successfully")
                     print(Style.RESET_ALL)
                     adoption_center.addPet(Pet(name,typePet,age,food,image1))
                     break

        elif choice == "6":
           
            print(Fore.LIGHTBLUE_EX,"Goodbye! Thanks for visiting our Adoption Center!\n")
            print(Style.RESET_ALL)
            break
            
        else:
            print(Fore.RED,"Invalid choice. Please try again.")
            print(Style.RESET_ALL)

