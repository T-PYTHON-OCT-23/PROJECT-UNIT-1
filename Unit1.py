# Project unit 1

# using dictionary for tickets
tickets = {
    "VIP",
    "Premium",
    "Gold",
    "Standard"}

for key in tickets:
    print(tickets)

tickets_price = {
    "VIP": "165$",
    "Premium": "115$",
    "Gold": "75$",
    "Standard": "35$"}

print(tickets)
ticket_input = input("Enter your ticket type: ")
if ticket_input in tickets:
    print(f"the cost of your ticket is {tickets_price[ticket_input]}")
else:
    print(f"Sorry we don't have the info for {tickets} ticket")


# using set for activities
user_input = input("click 'ENTER' to show all activities: ")

kids_set = {"Alice's Labyrinth", "Buzz", "Small World",
            "Advantage Isle", "Mad Hatter's", "PeterPan Dark"}
adult_set = {"Hyperspace mountain", "crush coaster",
             "Advantage Isle", "star tours", "Hollywood tower", "PeterPan Dark"}
all_ages = kids_set.intersection(adult_set)
disneyLand = kids_set.union(adult_set)

print("activities allowed just for kids: ", kids_set)
print("activities allowed just for adult: ", adult_set)
print("activities allowed for kids & adult together: ", all_ages)
print("All activities in Desney Land: ", disneyLand)


# using loop for activities conditions
visitor_height = input("Enter your height: ")
visitor_age = input("Enter your age: ")

for visitor in all_ages:
    if visitor_height < str(135) and visitor_age <= str(12):
        print(f"Enjoy kids activities! {kids_set}")
    elif visitor_height > str(135) and visitor_age >= str(13):
        print(f"Enjoy adult activities! {adult_set}")
    else:
        print("Sorry you can't Enter! this is Not Allowwd for you")


# using class to classify the object
user_input = input("click 'ENTER' to show more details about the activities: ")


class activity:
    def __init__(self, name, Ages, price, seats_available):
        self.name = name
        self.ages = Ages
        self.price = price
        self.seats = seats_available

    def instruction(self):
        instructions = f"this activity is {self.name}, it is allowed to enter for {self.ages}, its cost {self.price}, there is {self.seats} seats available"
        return instructions


activity1 = activity("Alice's Labyrinth", "Kids", "9$", 70)
activity2 = activity("Buzz", "Kids", "5$", 35)
activity3 = activity("Small World", "Kids", "6$", 45)
activity4 = activity("Advantage Isle", "Kids & adult", "10$", 85)
activity5 = activity("Mad Hatter's", "Kids", "5$", 35)
activity6 = activity("PeterPan Dark", "Kids & adult", "7$", 40)
activity7 = activity("Hyperspace mountain", "adult", "8$", 60)
activity8 = activity("crush coaster", "adult", "10$", 75)
activity9 = activity("star tours", "adult", "7$", 30)
activity10 = activity("Hollywood tower", "adult", "9$", 55)

print(activity1.name, activity1.ages, activity1.price, activity1.seats)
print(activity2.name, activity2.ages, activity2.price, activity2.seats)
print(activity3.name, activity3.ages, activity3.price, activity3.seats)
print(activity4.name, activity4.ages, activity4.price, activity4.seats)
print(activity5.name, activity5.ages, activity5.price, activity5.seats)
print(activity6.name, activity6.ages, activity6.price, activity6.seats)
print(activity7.name, activity7.ages, activity7.price, activity7.seats)
print(activity8.name, activity8.ages, activity8.price, activity8.seats)
print(activity9.name, activity9.ages, activity9.price, activity9.seats)
print(activity10.name, activity10.ages, activity10.price, activity10.seats)

print(activity1.instruction())
print(activity2.instruction())
print(activity3.instruction())
print(activity4.instruction())
print(activity5.instruction())
print(activity6.instruction())
print(activity7.instruction())
print(activity8.instruction())
print(activity9.instruction())
print(activity10.instruction())

# lambda
activities = [activity1, activity2, activity3, activity4,
              activity5, activity6, activity7, activity8, activity9, activity10]

def activity_addition(activity1, activity2): return activity1 + activity2
print("The sum of these two activities is: $" + str(activity_addition(9, 5)))

total_price = sum(map(lambda x: int(x.price.replace('$', '')), activities))
print(f"Total price of all activities: ${total_price}")
activity_price = []


# functions for seats booking
activities = [activity1, activity2, activity3, activity4,
              activity5, activity6, activity7, activity8, activity9, activity10]


def search_activities(activities, activity_name):
    for activity in activities:
        if activity.name == activity_name:
            return activity
        else:
            return "activity not found"


def seat_booking(activities, activity_name):
    activity_name = input("Enter the activity you want to book: ")

    found_activity = list(
        filter(lambda item: item.name == activity_name, activities))
    if len(found_activity) > 0 and found_activity[0].seats > 0:
        found_activity[0].seats -= 1
        print(f"You have successfully booked the activity {activity_name}, there is {found_activity[0].seats} seats available.")
    elif len(found_activity) > 0 and found_activity[0].seats == 0:
        print(f"the {activity_name} avtivity is full.")
    else:
        print("Invalid activity name. Please Enter an available activity.")

while True:
    seat_booking(activities)
    booking_again = input("Do you want to make another booking? (yes/no): ")
    if booking_again != "yes":
        print("good bye!")
        break

#exceptions 

def check_activity(activity_name):
    if activity_name == "maintenance":
        return ("Activity has maintenance")

activity_name = input("Enter the name of the activity: ")

try:
    check_activity(activity_name)
    print("Activity is good to go!")
except activity() as e:
    print(f"Error: {e}")


#using packages
from visitors import *
print(visitor1.name, visitor1.ages, visitor1.height)
print(visitor2.name, visitor2.ages, visitor2.height)
print(visitor3.name, visitor3.ages, visitor3.height)
print(visitor4.name, visitor4.ages, visitor4.height)
print(visitor5.name, visitor5.ages, visitor5.height)
print(visitor6.name, visitor6.ages, visitor6.height)

print(visitor1.identity())
print(visitor2.identity())
print(visitor3.identity())
print(visitor4.identity())
print(visitor5.identity())
print(visitor6.identity())