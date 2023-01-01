import math

print("Welcome to mu calculator")
print("Please choose one of these operators to continue")
print("+ = summation")
print("- = subtraction")
print("* = multiply")
print ("/ = devision")
print("pow = power")
print("sqrt = square root")
print("sin = sinus")
print("cos = cosinus")
print("tan = tangent")
print("cot = cotangent")
print("fac = factorial (You are allowed to enter positive integers ONLY!)")

op = input()
if op == "+" or op == "-" or op == "*" or op == "/" or op == "pow":
    a = float(input("Please enter your first number"))
    b = float(input("Please enter your second number"))
elif op == "fac":
    a= int(input("Please enter yor number"))
else:    
    a = float(input("Please enter your number"))    

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        result = "Cannot devide by zero"
    else:
        result = a / b
elif op == "pow":
    result = a ** b
elif op == "sqrt":
    if a < 0:
        result = "Cannot take roots from negative numbers"
    else:
        result = math.sqrt(a)  
elif op == "sin":
    result = math.sin(math.radians(a))
elif op == "cos":
    result = math.cos(math.radians(a))
elif op == "tan":
    result = math.tan(math.radians(a))
elif op == "cot":
    result = 1/(math.tan(math.radians(a)))
else:
    result = math.factorial(a)

print(result)

