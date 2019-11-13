# Unpacking: divide a list/tuples into variables
coordinates = (1, 2, 3)

x, y, z = coordinates
#x = coordinates[0]
#y = coordinates[1]
#z = coordinates[2]

print(x, y, z)

# Dictionnary
customer = {
    "name": "John",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Bob"
customer["gender"] = "male"
print(customer["name"], customer["gender"])  # .get("name") is the same
print(customer.get("birthdate", "Jan 1 1980"))

# Dictionnary example
message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😊",
    "':)": "😅"
}
output = ''
for word in words:
    output += emojis.get(word, word) + " "
print(output)


# Function
def message(first_name, last_name):  # first_name is one of the parameters
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print('Start')
message("Adam", "Douglas")  # without keywords arguments
# 'Mugiwara' is an argument of the parameter name (with keyword arguments)
message(last_name="No Luffy", first_name="Mugiwara")
print('Finish')


def square(number):
    return f'The square is {number*number}.'  # without return = 'None'


print(square(int(input('Enter a number: '))))

# Dictionary and function


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        "':)": "😅"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))

try:
    age = int(input('Age: '))
    print(age)
except ZeroDivisionError:
    print("Age must be more than 0.")
except ValueError:
    print("Oups, what did you do?")

# Class
class Point:
    def __init__(self, x, y):  # Constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 15
print(point2.x)

point = Point(10, 20)
print(point.x)

# Inheritance
class Mother:
    def run(self):
        print("Run")


class Cat(Mother):
    pass  # to prevent from "empty class"


class Human(Mother):
    def be_annoying(self):
        print("Be annoying.")


al = Human()
al.be_annoying()