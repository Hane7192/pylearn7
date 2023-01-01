import turtle
import random

n = 3 
p = turtle.Pen()


while n >= 3:
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    p.pencolor(red/255 , green/255 , blue/255)

    degree = (n - 2)* 180 / n
    
    p.left(180-degree/2)
    
    for i in range(n):
        p.forward(70* (1+ n/10))
        p.left(180-degree)
        
    
    p.right(180-degree/2)
    p.penup()
    p.forward(12* (1+ n/10))
    p.pendown()
    n += 1
    