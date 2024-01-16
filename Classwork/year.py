##year = 2019
##year = year + 1
##print(year)


import turtle
shape = turtle.Turtle()
sidesimp=(input("Number of Sides?")
sides= int(sidesimp)
color = input("Color")
       
D=(360/sidesnumb)
S=(100)

##x=(-200)
##y=(200)       
##shape.penup()
##shape.goto(x, y)
##shape.pendown()
shape.fillcolor(color)
shape.begin_fill()
shape.pensize(2)
shape.pencolor("blue")
for side in range (sides):
    shape.forward(S)
    shape.right(D)

shape.end_fill()
