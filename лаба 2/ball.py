from turtle import *


shape('circle')
shapesize(0.5)

vx = 30 
vy = 50
alpha = 0.8



x = [0] * 400
y = [0] * 400


ht()
penup()
speed(0)
goto(300, 0)
pendown()
goto(-300, 0)
st()

for j in range(5):
    vy *= alpha ** j
    vx *= alpha ** j
    dt = vy / 2000 # dt = (vy/g)/2/100
    N = int(2 * (vy / 10) / dt)
    x[0] = x[N-1]
    
    for i in range(0, N):
        x[i] = x[0] + vx * i * dt 
        y[i] = y[0] + vy * (i * dt) - 10 * ((i * dt) ** 2) / 2
        goto(x[i] - 300, y[i])




