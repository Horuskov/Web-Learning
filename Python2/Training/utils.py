def find_max(number):
    numbers = [int(i) for i in number]
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max
