# age should be over 18 and under 70
age = 24

message = "Eligible." if age >= 18 else "Not eligible."
print(message)
if 18 <= age < 70:  # chaining comparison operator
    print("Eligible.")


for x in range(1, 10):
    if x % 2 == 0:
        print(x)
print("We have 4 even numbers")

i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

for item in ['Basile', 'Smart', 'Jerry']:
    print(item)

names = ['Joe', 'Jack', 'Johnny']
print(
    f"\nThe first element is 0, the second is 1 and so on. The list: {names}.")
print(names[int(input("\nSelect a name index: "))])

#Tuples (immutable: cannot be changed)
numbers = (1,2,3)


# 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

numbers = [5, 3, 6]
numbers2 = numbers.copy()
numbers2.append(99999)

numbers.append(20)
numbers.insert(0, 6)
# .clear() to remove everything .pop() to remove the last nbr
numbers.remove(3)
print(f'6 appears: {numbers.count(6)} times.')
# '20 in numbers' check if 20 is present (True) or not (False)
print(f'20 is located at the position n°{numbers.index(20)} in the list.')
print(f'Here is the list: {numbers}.')
numbers.sort()  # can't be used in a function
print(f'Here is the sorted list: {numbers}.')
numbers.reverse()
print(f'Here is the ascended sorted list: {numbers}.')
print(f'Here is the second list (unchanged): {numbers2}.')
