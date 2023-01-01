def generate_rug(num):

    m = n = num 
    k = 0 
    l = 0 
    i = 0 

    if num % 2 == 1 and num > 1:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        colors = ["🧡","💛","💚","💙","💜","🤎","🤍"]

        if num > 7:
            colors = colors * (num//7 +1)

        while k < m and l < n :  
        
            for i in range(l, n) :      
                if matrix[k][i] == 0:
                    matrix[k][i] = colors[k]   

            k += 1   

            for i in range(k, m) :         
                if matrix[i][n-1]==0:
                    matrix[i][n-1] = colors[k-1]  
            n -= 1   

            if (k<m):  
                for i in range(n-1, l-1, -1):
                    if matrix[m-1][i] == 0:
                        matrix[m-1][i] = colors[k-1]  
            m -= 1  

            if (l<n):    
                for i in range(m-1, k-1, -1):
                    if matrix[i][l] == 0:
                        matrix[i][l] = colors[k-1]
            l += 1   

            num -= 1    

        return matrix
    
    else: 
        return ["you can just enter an odd number"]

for rows in generate_rug(int(input("Enter the number of rows and columns: "))):
    print(rows)