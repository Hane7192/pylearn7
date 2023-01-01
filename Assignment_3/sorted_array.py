length = int(input("Enter the length of your array: "))
array = []
j = 0

for i in range(length):
    new_num = int(input("Enter a number: "))
    array.append(new_num)

print("your array is :", array)

for i in range (length - 1):
    if array[i] < array[i+1]:
        j += 1

if j == length - 1:
    print("your array is sorted")

else :
    print("your array is not sorted")
