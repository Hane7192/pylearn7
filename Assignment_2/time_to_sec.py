q = "Yes"

while q == "Yes":
    h = int(input("Enter the hour : "))
    m = int(input("Enter the minute : "))
    s = int(input("Enter the second : "))

    result = (h * 3600) + (m * 60) + s
    print ("%.2d" % h , ":" , "%.2d" % m , ":" , "%.2d" % s , "=" , result , "seconds")
    print("Do you want to continue? ")
    q = input("Type Yes to continue and No to exit : ")


