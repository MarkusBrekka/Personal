# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:37:16 2023

@author: marku
"""

import turtle
import math

x_akse = float(input("Hvor på x-aksen ønsker du ditt imaginære punkt? [3,3]"))
y_akse = float(input("Hvor på i-aksen ønsker du ditt imaginære punkt? [-3,3]"))

turtle.setup(800,950,750,0)

def notasjoner():
    turtle.forward(300)
    for i in range(0,3):
        turtle.left(90)
        turtle.forward(10)
        turtle.left(180)
        turtle.forward(20)
        turtle.left(180)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(100)
        if i == 0 or 2:
            turtle.left(180)
        else:
            print("ok")
            
def punkt():
    turtle.left(45)
    for i in range(0,4):
        turtle.forward(5)
        turtle.left(180)
        turtle.forward(5)
        turtle.left(90)

turtle.speed(10)       

for i in range(0,4):
    notasjoner()
    turtle.left(90)



turtle.penup()
turtle.left(90)
turtle.forward(y_akse*100)
turtle.right(90)
turtle.forward(x_akse*100)
turtle.pendown()
punkt()

argument = math.atan(y_akse/x_akse)
argument_degrees = math.degrees(argument)
turtle.setheading(90)


turtle.left(argument_degrees)

    
turtle.circle((math.sqrt(x_akse**2 + y_akse**2)*100))
print(argument)
print(argument_degrees)


turtle.exitonclick()