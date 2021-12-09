from random import randint
import turtle 

wn = turtle.Screen()     #задание экрана
wn.tracer(0)            #обновление экрана

turtle.speed(0)          #границы сосуда
turtle.ht()
turtle.pu()
turtle.goto(-300, -300)
turtle.pd()             
for i in range(4):
    turtle.fd(600)
    turtle.lt(90)

number_of_turtles = 13

vessel = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for molecule in vessel:
    molecule.pu()
    molecule.speed(0)
    molecule.goto(randint(-200, 200), randint(-200, 200))
    molecule.lt(randint(1, 360))
    molecule.dy = (0.1 * randint(-10, 10))
    molecule.dx = (0.1 * randint(-10, 10))
    if molecule.dy == 0:
        molecule.dy = 0.5
    if molecule.dx  == 0:
        molecule.dx = 0.5

while True:
    wn.update()
    for molecule in vessel:
        molecule.sety(molecule.ycor() + molecule.dy)
        molecule.setx(molecule.xcor() + molecule.dx)
        if molecule.ycor() < -300:
             molecule.dy *= -1
        elif molecule.ycor() > 300:
             molecule.dy *= -1
        elif molecule.xcor() < -300:
            molecule.dx *= -1
        elif molecule.xcor() > 300:
            molecule.dx *= -1
        for another_molecule in vessel:
            q = molecule.dy
            w = molecule.dx
            e = another_molecule.dy
            r = another_molecule.dx
            d = (molecule.ycor() - another_molecule.ycor()) ** 2 + (molecule.xcor() - another_molecule.xcor()) ** 2
            if 0 < d < 20:
                if q > 0:
                    while molecule.dy > -1 * q:
                        molecule.dy -= 0.5
                elif q < 0:
                    while molecule.dy < -1 * q:
                        molecule.dy -= 0.5
                elif w > 0:
                    while molecule.dy > -1 * w:
                        molecule.dy -= 0.5
                elif w < 0:
                    while molecule.dy < -1 * w:
                        molecule.dy -= 0.5
                elif e > 0:
                    while molecule.dy > -1 * e:
                        molecule.dy -= 0.5
                elif e < 0:
                    while molecule.dy < -1 * e:
                        molecule.dy -= 0.5
                elif w > 0:
                    while molecule.dy > -1 * q:
                        molecule.dy -= 0.5
                elif w < 0:
                    while molecule.dy < -1 * q:
                        molecule.dy -= 0.5
       
                                                    




     

