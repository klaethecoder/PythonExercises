import turtle
from turtle import *

answer = input("Would you like to see a star or a circle? ").lower()

def drawSquare(turtle):
    counter = 1
    while counter <=4:
        turtle.forward(100)
        turtle.right(90)
        counter+= 1

def drawing():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = Turtle()
    brad.speed(15)
    brad.shape("turtle")
    brad.color("yellow")
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

drawing() if answer == "circle" else starShape()