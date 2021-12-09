from turtle import *
shape('turtle')
n = int(input())
for i in range (n):
    forward(70)
    stamp()
    backward(70)
    left(360/n)
