# using packages 

class visitors:
    def __init__(self, name, Ages, height):
        self.name = name
        self.ages = Ages
        self.height = height

    def identity(self):
        hello = f"Hello my name is {self.name}, I've {self.ages} years old, my height is {self.height}cm. "
        return hello

visitor1 = visitors("Ahmed", "23", "179")
visitor2 = visitors("Nora", "18", "157")
visitor3 = visitors("Amal", "27", "159")
visitor4 = visitors("Mariam", "11", "133")
visitor5 = visitors("Osama", "25", "183")
visitor6 = visitors("Rami", "8", "127")
