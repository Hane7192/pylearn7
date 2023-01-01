firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")
a = float(input("Enter the first score: "))
b = float(input("Enter the second score: "))
c = float(input("Enter the third score: "))

ave = (a + b + c)/3

if ave >= 17:
    result = "Great"
elif ave >= 12:
    result = "Normal" 
else:
    result = "Fail" 

print("the GPA of" , firstname , lastname , "is", result)
