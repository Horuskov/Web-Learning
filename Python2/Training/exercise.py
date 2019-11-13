# first exercise
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizz_buzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input
print(fizz_buzz(5))

# second
name = input('What is your name? ')
color = input('What is your favorite color? ')
print(name + ' likes ' + color + '.')

# third
weight = float(input("What is your weight (in pounds)? "))
kg = 0.453592
print(f'Your weight is {round((weight * kg))} kg.')

# Guess game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("Well played!")
        break
else:
    print("You failed!")

# Weight program
weight = int(input('Weight: '))
convertor_kg = 0.45
lbs_kg = input('(L)bs or (K)g: ')
if lbs_kg.upper() == 'L':
    converted = round(weight*convertor_kg, 1)
    print(f'You are {converted} kilos')
else:
    converted = round(weight/convertor_kg, 1)
    print(f'You are {converted} pounds')

# Marriage
married = bool(int(input(
    "Are you married, mofo ? Type: [1 for YES] // [0 for NO]:")))
nbr_couple = input("Enter number of couple going to marry:")
print(married)
widow = False
over_eighteen = True
version = "Try number: "

if (widow or over_eighteen) and not married:
    print('Can marry')
else:
    print('Cannot marry')

for number in range(1, 6, 1):
    print("Hello?", f"{version}{number}", number*".")

for number in range(int(nbr_couple)):
    if married == False:
        print("you may kiss the bride.")
    if married:  # == True by default
        print("but if you're married: you may go to hell, Satan's collaborator.")
        break
else:
    print('Every couple s member where not married before marrying')



# Car game
command = ""
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started....Ready to go!")
    elif command == 'stop':
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped.")
    elif command == 'quit':
        quit = 'You got off the car.'
        print(quit)
    elif command == 'help':
        help = '''enter - to get in the car
start - to start the car
stop - to stop the car
quit - to get off the car'''
        print(help)
    elif command == 'quit':
        break
    else:
        print("Hey, I don't understand that. Enter 'help' for more... help.")


# Caculate total of prices
prices = [10, 20, 30]
total = 0

for price in prices:
    print(price)

    import math
import random


#Standard version of largest number in a list
ages = [2, 3, 4, 8, 3, 9]
largest_number = 0

for number in ages:
    if number > largest_number:
        largest_number = number
print(largest_number)

#Advanced version of largest number in a list (with random)
ages = []
largest_number = 0

for x in range(20):
    ages.append(int(random.randint(1, 101)))
    if ages[x] > largest_number:
        largest_number = ages[x]
print(ages)
print(largest_number)

#Retirer les nombres doubles
numbers = [2, 2, 4 ,6, 3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# Translate phone number digits into literal "One", "Two"...
numbers = {
    "1": "One",
    "2": "Two"
}

phone = input("Phone: ")
output = ''
for char in phone:
    output += numbers.get(char, "!") + " "
print(output)