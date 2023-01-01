def chessboard(n , m):

    finalSentence1 = ""
    finalSentence2 = ""

    for i in range(m): 
        
        if i%2 == 0: 
            finalSentence1 += "*"
            finalSentence2 += "#"
        else:
            finalSentence1 += "#"
            finalSentence2 += "*"


    for j in range(n):
       
        if j%2 == 0:
            print(finalSentence1)
        else:
            print(finalSentence2)

chessboard(int(input("Enter the number of rows : ")) , int(input("Enter the number of columns : ")))