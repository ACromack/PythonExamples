import turtle

wn = turtle.Screen()
#wn.bgcolor("orange")

t = turtle.Turtle()
t.shape("turtle")


from math import sin,cos,pi
def ellipse(pen, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    penX, penY = pen.pos()
    for i in range(0, 360):
        penX += cos(i*pi/180)*width
        penY += sin(i*pi/180)* (height/2)
        pen.goto(penX, penY)
    pen.penup()


turtle.tracer(0,0)
#turtle.update()

t.color("red")
t.begin_fill()
for x in range(3):
    t.forward(50)
    t.right(120)
t.end_fill()

t.up()
t.setpos(100,60)

t.down()
t.color("blue")
t.begin_fill()
for x in range(6):
    t.forward(50)
    t.right(60)
t.end_fill()

t.up()
t.setpos(-200,60)

t.down()
t.color("orange")
t.begin_fill()
for x in range(12):
    t.forward(50)
    t.right(30)
t.end_fill()

t.up()
t.setpos(0, 100)
t.stamp()
t.setpos(0, 200)

t.down()
t.color("black")
ellipse(t,0,0,1,1)
