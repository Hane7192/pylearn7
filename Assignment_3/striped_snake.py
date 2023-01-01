n = int(input("Enter the length of your snake 🐍: "))
array = []

while len(array) < n:
    array.append("*")
    array.append("#")

for i in range (n):
    print(array[i], end ="")