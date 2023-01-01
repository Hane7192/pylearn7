firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")
score = 0
n = 0

while True: 
    a = input("Enter the score or Type exit to calculate the GPA: ")
    if a == "exit":
        break
    else:
        score = score + float(a)
        n = n + 1
    

ave = score/n
print("the GPA of" , firstname , lastname , "is", ave)
