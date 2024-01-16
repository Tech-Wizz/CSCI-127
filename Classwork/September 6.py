import turtle

#-----------------------------


#star = turtle.Turtle()
#star.color("pink")

#star2 = turtle.Turtle()
#star2.color("blue")

#star3 = turtle.Turtle()
#star3.color("green")

#star4 = turtle.Turtle()
#star4.color("yellow")

#-----------------------------


SIDES = 5   #number of sides on a star, a constant 

def draw_star(the_turtle):
    the_turtle.penup()
    the_turtle.forward(350)
    the_turtle.pendown()
    the_turtle.right(144)
    for i in range(SIDES):
        the_turtle.forward(100)
        the_turtle.right (180 - 180/SIDES)  #calculate the turn angle
    the_turtle.end_fill()

#-----------------------------


def main():
    star = turtle.Turtle()
    star.color("pink")
    window = turtle.Screen()
    window.bgcolor("light green")
    star.penup()
    star.goto(-175,0)
    star.pendown()

    for i in range(5):
        draw_star(star)

main()

#-----------------------------

#draw_star(star, 0, 200)
#draw_star(star2, 0, 0)
#draw_star(star3, -200, 0)
#draw_star(star4, -200, 200)
