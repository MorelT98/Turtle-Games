from turtle import *
from base import Vector
from random import randrange

class Ball(Vector):
    def __init__(self, x, y, aim=Vector(-1, 0)):
        super(Ball, self).__init__(x, y)
        self.aim = aim



ball = Ball(0, -100, aim=Vector(0, -1))
itr = 0
pipes = []
BALL_SIZE = 10
BALL_COLOR = 'green'
PIPE_SIZE = 20
PIPE_COLOE = 'black'

def in_bounds(ball):
    return -190 <= ball.x <= 300 and -195 <= ball.y <= 220

def game_over():
    # If the ball goes out of bounds
    if not in_bounds(ball):
        return True

    # If the ball hits a pipe
    for pipe in pipes:
        if abs(pipe - ball) < PIPE_SIZE / 2:
            return True

    return False

def draw():
    global itr

    if game_over():
        up()
        goto(140, 160)
        color('red')
        write('Game Over')
        update()
        return

    clear()
    # draw the ball
    up()
    goto(ball.x, ball.y)
    dot(BALL_SIZE, BALL_COLOR)

    # draw the pipes:
    for pipe in pipes:
        up()
        goto(pipe.x, pipe.y)
        dot(PIPE_SIZE, PIPE_COLOE)

    # display the score
    up()
    goto(140, 180)
    write('Score: {}'.format(itr // 20))
    update()

    # move the ball
    ball.move(ball.aim)

    # remove out of bounds pipes
    init_length = len(pipes)
    for i in range(init_length):
        if i in range(len(pipes)) and not in_bounds(pipes[i]):
            pipes.remove(pipes[i])
            if i > 0:
                i -= 1

    # move the pipes
    for pipe in pipes:
        pipe.move(pipe.aim)

    # add new pipes
    if randrange(100) < 5:
        pipe = Ball(200, randrange(-200, 200))
        pipes.append(pipe)

    # update the score
    itr += 1

    ontimer(draw, 20)

setup(420, 420)
hideturtle()
tracer(False)
draw()
listen()
onkeypress(lambda : ball.move(Vector(0, 30)), 'space')
done()