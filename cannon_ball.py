from random import *
from turtle import *
from base import Vector

ball = Vector(-200, -200)
speed = Vector(0, 0)
targets = []

def inside(x_y):
    return -200 < x_y.x < 200 and -200 < x_y.y < 200

def tap(x, y):
    # Respond to the screen
    if not inside(ball):    # Only relaunch the ball when it goes out of frame
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def draw():
    # draw the ball and the targets
    clear()
    # draw targets
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
    # draw ball if it's inside the frame
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# movement of ball and target
def move():
    # Create random targets
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = Vector(200, y)
        targets.append(target)

    # Move each target
    for target in targets:
        target.x -= 0.5

    # Move the ball
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dup = targets.copy()
    targets.clear()

    # Only save the targets that are not touching the ball
    for target in dup:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Stop the game when one targets reaches the end of the frame
    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

# Hides the turtle (mouse icon)
hideturtle()

# Removes the lines in between objects
up()

# Removes any delay in drawings update, so make the balls move smoothly
tracer(False)

onscreenclick(tap)
move()
done()


setup(420, 420, 370, 0)