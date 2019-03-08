import turtle
from turtle import *

def drawSquare(turtle):
    counter = 1
    while counter <=4:
        turtle.forward(100)
        turtle.right(90)
        counter+= 1

def drawing():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.speed(15)
    # angie = turtle.Turtle()
    # fred = turtle.Turtle()
    brad.shape("turtle")
    # angie.shape("turtle")
    # fred.shape("turtle")
    brad.color("yellow")
    # angie.color("yellow")
    # fred.color("blue")
    for i in range(1,37):
        drawSquare(brad)
        brad.right(10)

    window.exitonclick()

def starShape():
    Screen()
    speed(20)
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    exitonclick()

drawing()
# starShape()