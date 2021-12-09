from turtle import *
shape('turtle')


for i in range(1, 101, 10):
    penup()
    goto(-i,-i)
    pendown()
    for step in range(4):
        forward(50+2*i)
        left(90)
    
   
