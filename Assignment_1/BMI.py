w = float(input("Enter your Weight(kg) "))
h = float(input("enter your height(m) "))

BMI = w/(h**2)

if BMI >= 35 and BMI < 40:
    result = "Extreme Obesity"
elif BMI >= 30:
    result = "Obesity"
elif BMI >= 25:
    result = "Overweight"  
elif BMI >= 18.5:
    result = "Normal Weight"
elif BMI < 18.5:
    result = "underweight"    

print(result)