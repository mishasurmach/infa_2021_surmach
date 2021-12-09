from turtle import *
import numpy as np

shape('turtle')

def regular_polygon(n):
        for mumber in range(n):
            forward(r*2*np.sin(260/(2*n)))
            left(360/n)
            
for r in range (10, 70, 10):
    for i in range(3, 10):
        regular_polygon(i)
    
    


