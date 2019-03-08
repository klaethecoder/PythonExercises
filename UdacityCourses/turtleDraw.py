import turtle

def drawing():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    angie = turtle.Turtle()
    fred = turtle.Turtle()
    brad.shape("turtle")
    angie.shape("turtle")
    fred.shape("turtle")
    brad.color("green")
    angie.color("yellow")
    fred.color("blue")
    counter = 1
    angie.circle(200)
    fred.circle(100)
    while counter <=4:
        brad.forward(100)
        brad.right(90)
        counter+= 1
    window.exitonclick()

drawing()

# def draw():
#      window = turtle.Screen()
#      window.bgcolor("red")
#      brad = turtle.Turtle()
#      turtle.begin_fill()
#      brad.forward(100)

# # print(dir(turtle))
# draw()