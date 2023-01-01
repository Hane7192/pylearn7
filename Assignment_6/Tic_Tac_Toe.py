import pyfiglet 
import random
from termcolor import colored
import timeit

def show():
    for row in gameboard:
        for cell in row:
            print(cell, end=" ")
        print()

def check_game():
    x = False
    for row , col in zip(range(0,3), range(0,3)):
            if gameboard[row][0] == gameboard[row][1] == gameboard[row][2] != "_" or gameboard[0][col] == gameboard [1][col] == gameboard[2][col] != "_":
                x = True
    if x or gameboard[0][0] == gameboard[1][1] == gameboard[2][2] != "_" or gameboard[2][0] == gameboard[1][1] == gameboard[0][2] != "_":
        print(winner, "wins!")
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        exit()
    elif not any("_" in i for i in gameboard):
        print("Draw")
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        exit()
    
title = pyfiglet.figlet_format("Tic Tak Toe", font = "slant")

print(title)
print("Welcome to Tic Tac Toe...")
print("For palying with Computer Press 1  ")
print("For Playing with Another Player Press 2 ")
player2_type = int(input())

gameboard = [ ["_" , "_" , "_"] ,
              ["_" , "_" , "_"] ,
              ["_" , "_" , "_"] ]
show()

while True:
    start = timeit.default_timer()
    print("palyer 1: ")
    
    while True:
        row = int(input("row :"))
        col = int(input("col :"))
        
        if 0 <= row <= 2 and 0 <= col <= 2:
            if gameboard[row][col] == "_":
                gameboard[row][col] = colored("X", "red")
                break
            else:
                print("This block has been chosen before. Try another one")
        else:
            print("You are just allowed to choose a number between 0 and 2")
    show()
    winner = "player 1"
    check_game()

    if player2_type == 2:
        print("palyer 2: ")
        
        while True:
            row = int(input("row :"))
            col = int(input("col :"))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if gameboard[row][col] == "_":        
                    gameboard[row][col] = colored("O", "blue")
                    break
                else: 
                    print("This block has been chosen before. Try another one")
            else:
                print("You are just allowed to choose a number between 0 and 2")

        show()
        winner = "player 2"
        check_game()

    elif player2_type == 1:
        print("player 2: ")
        while True:

            row = random.randint(0 , 2)
            col = random.randint(0 , 2)
            
            if gameboard[row][col] == "_":        
                gameboard[row][col] = colored("O", "blue")
                break

        show()
        winner = "Computer"
        check_game()
