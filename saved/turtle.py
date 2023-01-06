import turtle
from time import sleep

# show turtle in the center by default. East by default, turtle with arrow as head
turtle.showturtle()

# move forward for 100px, i.e. right
turtle.forward(100)
sleep(0.5)

# turn left on 90d. i.e. clockwise, degrees depends on current position
turtle.left(90)
turtle.forward(100)  # move forward
sleep(0.5)

# show current arrow direction
print(turtle.heading())

# set new direction frod default=0 to 180
turtle.setheading(180)
turtle.forward(100)
sleep(0.5)

turtle.left(90)
turtle.forward(100)
sleep(0.5)

# i can shape it as:square, circle, triangle, arrow, classic, turtle
turtle.backward(50)
turtle.shape('turtle')
sleep(1)
turtle.setheading(0)


def rectangle(width, height):
    for _ in range(4):
        turtle.forward(width)
        sleep(0.5)
        turtle.right(90)
        width, height = height, width


def triangle(side):
    turtle.left(30)
    turtle.forward(side)
    sleep(0.5)
    turtle.setheading(180)
    turtle.right(30)
    turtle.forward(side)
    sleep(0.5)
    turtle.setheading(270)
    turtle.forward(side)
    sleep(0.5)

rectangle(50, 50)
triangle(50)


###############################################################################

# 1. 8 squares
def square(side):
    for _ in range(4):
        turtle.forward(side)
        sleep(0.05)
        turtle.left(90)

side = 100

turtle.shape('arrow')

for _ in range(8):
    turtle.left(45)
    square(side)

# 2.
import turtle

def hexagon(side):
    turtle.forward(side / 2)
    for _ in range(5):
        turtle.left(60)
        turtle.forward(side)
    turtle.left(60)
    turtle.forward(side / 2)

side = 100

hexagon(side)

# 3.
import turtle

def hexigen(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)

def honey():
    for _ in range(6):
        hexigen(side)
        turtle.right(120)
        turtle.forward(side)
        turtle.left(60)

side = 100

honey()

# 4.
