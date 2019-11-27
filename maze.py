from turtle import *
from random import *
from base import line

def draw():
    # drawing a maze
    color('black')

    # width of the maze
    width(10)
    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            # create either a line going diagonally up...
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            # ...or diagonally down
            else:
                line(x, y + 40, x + 40, y)
    update()

def tap(x, y):
    # draw line and dot in the screen when you tap
    if abs(x) > 198 or abs(y) > 198:
        up()
    else:
        down()
    width(2)
    color('red')
    goto(x, y)
    dot(4)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()