import random

user_score = 0
computer_score = 0
r = 0

while user_score < 5 and computer_score < 5:
   
    x = random.randint(1, 3)

    if x == 1:
        computer_choice = "rock"
    elif x == 2:
        computer_choice = "paper"
    elif x == 3:
        computer_choice = "scissors"

    user_choice = input("enter your choice: rock, paper or scissors? ")  

    if computer_choice == "rock" and user_choice == "paper":
        user_score = user_score + 1

    elif computer_choice == "rock" and user_choice == "scissors":
        computer_score = computer_score + 1

    elif computer_choice == "rock" and user_choice == "rock":
        print("try again")

    elif computer_choice == "paper" and user_choice == "rock":
        computer_score = computer_score + 1

    elif computer_choice == "paper" and user_choice == "scissors":
        user_score = user_score + 1

    elif computer_choice == "paper" and user_choice == "paper":
        print("try again")

    elif computer_choice == "scissors" and user_choice == "rock":
        user_score = user_score + 1

    elif computer_choice == "scissors" and user_choice == "paper":
        computer_score = computer_score + 1

    elif computer_choice == "scissors" and user_choice == "scissors":
        print("try again")    
    
    r = r + 1 
    print("computer's choice is :" , computer_choice)
    print("You :", user_score , "computer :" , computer_score)  

if user_score > computer_score:
    print("You won after", r , "attempts")
else:
    print("Sorry! computer won after" , r , "attempts")
