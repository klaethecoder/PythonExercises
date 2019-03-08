import turtle
from turtle import *


def drawSquare(turtle):
    counter = 1
    while counter <=4:
        turtle.forward(100)
        turtle.right(90)
        counter+= 1

def drawFlower(turtle):
    counter = 1
    while counter <=2:
        turtle.forward(80)
        turtle.right(30)
        turtle.forward(80)
        turtle.right(150)
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

def flower():
    window = Screen()
    window.bgcolor("gray")
    fred = Turtle()
    fred.speed(15)
    fred.color("red")
    for i in range(1,37):
        drawFlower(fred)
        fred.right(10)
    fred.color("yellow")
    for i in range(1,4):
        fred.circle(35)
        fred.right(120)
    fred.color("green")
    fred.shape("square")
    fred.right(90)
    fred.forward(250)
    window.exitonclick()

answer = input("Would you like to see a star or a circle? ").lower()
drawing() if answer == "circle" else starShape()
# flower()