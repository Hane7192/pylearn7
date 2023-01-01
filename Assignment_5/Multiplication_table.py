def Multiplication_table(n , m):

    for i in range(1 , n + 1):
        for j in range(1 , m + 1):
            result = i * j
            
            if result < 10:
                print(result ," ", end = "")
            else:
                print(result ,"", end = "")
        j = 1
        print()

Multiplication_table(int(input("Enter the number of rows : ")) , int(input("Enter the number of columns : ")))