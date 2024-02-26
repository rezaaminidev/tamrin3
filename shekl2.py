import turtle

turtle.getscreen()
t = turtle.Turtle()
a = 20


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(80):
    a += 5
    t.left(20)
    t.forward(15)

   
    t.fillcolor(colors[i % len(colors)])
    t.begin_fill()  

    for j in range(4):
        t.forward(a)
        t.left(90)

    t.end_fill()  

turtle.done()
