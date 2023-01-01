import random

n = int(input("Enter your desired length: "))
array = []

while len(array) < n:
    new_num = random.randint(0, 100)
    if new_num not in array:
        array.append(new_num)

print (array)