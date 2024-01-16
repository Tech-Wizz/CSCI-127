#------------------------------------+
#Kruize Christensen                  |
#Lecture:September 4, 2019           |
#------------------------------------+
#Let the user move a turtle around   |
#------------------------------------+

import turtle

window = turtle.Screen()

drawer = turtle.Turtle()
drawer.speed(0)

def east():
    drawer.setheading(0)
    drawer.forward(50)

def north():
    drawer.setheading(90)
    drawer.forward(50)

def west():
    drawer.setheading(180)
    drawer.forward(50)

def south():
    drawer.setheading(270)
    drawer.forward(50)

def right():
    drawer.right(45)

def forward():
    drawer.forward(50)

window.onkey(east, "Right")
window.onkey(north, "Up")
window.onkey(west, "Left")
window.onkey(south, "Down")
window.onkey(right,"R")
window.onkey(right,"r")
window.onkey(forward,"F")
window.onkey(forward,"f")
window.listen()

window.exitonclick()
