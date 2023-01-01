a = float(input("Enter the length of the first side : "))
b = float(input("Enter the length of the second side : "))
c = float(input("Enter the length of the third side : "))

if a + b > c and a + c > b and b + c > a:
    print("You can draw a triangle with given lenght")
else:
    print("You cannot draw a triangle with given lenght")    