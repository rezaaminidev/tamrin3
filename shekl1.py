import turtle

turtle.getscreen()
t = turtle.Turtle()
t.speed(1)
a=200
b=4

for i in range(80):
    a=a-b
    t.forward(a)
    t.left(90)
