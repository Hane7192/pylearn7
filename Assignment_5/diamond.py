def diamond(n):

    for i in range (n - 1 , -1 , -1):
        spaces = " " * i
        stars = "*" * (2 * n - (2 * i + 1))
        print(spaces, stars)
            
    # for j in range (1 , n + 1):        
            
    #     spaces = " " * (j)
    #     stars = "*" * (2 * n - (2 * j + 1))
    #     print(spaces, stars)

diamond(int(input("Enter the number of rows : ")))