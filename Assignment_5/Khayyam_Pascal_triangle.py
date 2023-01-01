def khayyam_pascal_triangle(n):
    
    KPT = [[1]]
    print(KPT [0]) 
    
    for i in range(1 , n):
        KPT.append([1]) 

        for j in range(len (KPT[i - 1] ) - 1):
        
            KPT[i].append(KPT[i - 1][j] + KPT[i - 1][j + 1])
            
        KPT[i].append(1) 
        print(KPT[i])

khayyam_pascal_triangle(int(input("Enter the number of iterations: ")))