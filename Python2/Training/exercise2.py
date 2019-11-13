import random

#Create a Class
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi folks, I must be {self.name}.")


john = Person("John Smithee")
john.talk()

bob = Person("Bob Marley")
bob.talk()

# Module exo
from utils import find_max

number = input("Enter a sequel of numbers: ")
# max = find_max(number)
print(max(number))

# Built a dice
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second #Make a tuple


dice = Dice()
print(dice.roll())
