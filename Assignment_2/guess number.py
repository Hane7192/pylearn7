import random

computer_number = random.randint(1, 100)

for i in range(10):
    user_number = int(input("Enter a number:"))

    if computer_number == user_number:
        print("Congradulations! You won after" , i+1 , "attempts")
        break

    elif computer_number > user_number:
        print("go up ⏫")

    elif computer_number < user_number:
        print("go down ⏬ ")   

         
