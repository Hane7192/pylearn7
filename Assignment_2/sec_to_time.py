q = "Yes"

while q == "Yes":
    a = int(input("Enter the nember of seconds : "))
    h = (a // 3600)
    m = ((a % 3600) // 60)
    s = ((a % 3600) % 60)
    
    print(a , "seconds equals" , "%.2d" % h ,":" , "%.2d" % m , ":" , "%.2d" % s )
    print("Do you want to continue? ")
    q = input("Type Yes to continue and No to exit : ")