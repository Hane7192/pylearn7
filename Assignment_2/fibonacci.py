n = int(input("How many terms of series are required? "))
a0 = 0
a1 = 1


print(a1, end ="")
    
for i in range(2 , n+1):
        
    an = a0 + a1
    print(",", an , end ="")
    a0 = a1
    a1 = an
    


