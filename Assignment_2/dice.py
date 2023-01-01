import random

while input("Do you want to play? Yes/No ") == "Yes":
    a = random.randint(1 , 6)
    print("🎲 : ", a)
    while a == 6:
        print("Hooray! You have another chance!")
        input("Press enter to roll the dice")
        a = random.randint(1 , 6)
        print("🎲 : ", a)