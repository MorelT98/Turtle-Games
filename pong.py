from turtle import *
from base import Vector, line
from random import random

PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20
BALL_SIZE = 15
BALL_RADIUS = BALL_SIZE / 2
BG_COLOR = 'green'
COLOR = 'white'

paddle_1 = Vector(-200, -PADDLE_HEIGHT / 2)
paddle_2 = Vector(200 - PADDLE_WIDTH, -PADDLE_HEIGHT/2)
ball = Vector(0, 0)
ball_aim = Vector(random() * 2 - 1, random() * 2 - 1) * 3

def rectangle(x, y, width, height):
    color(COLOR)
    begin_fill()
    line(x, y, x + width, y)
    line(x + width, y, x + width, y + height)
    line(x + width, y + height, x, y + height)
    line(x, y + height, x, y)
    end_fill()
    color(BG_COLOR)

# checks if ball hits top or bottom wall
def hits_wall(ball):
    return ball.y + BALL_RADIUS >= 200 or ball.y - BALL_RADIUS <= -200

# check if ball hits any of the paddles
def hits_paddle(ball):
    hits_paddle_1 = ball.x - BALL_RADIUS <= paddle_1.x + PADDLE_WIDTH and paddle_1.y < ball.y < paddle_1.y + PADDLE_HEIGHT
    hits_paddle_2 = ball.x + BALL_RADIUS >= paddle_2.x and paddle_2.y < ball.y < paddle_2.y + PADDLE_HEIGHT
    return hits_paddle_1 or hits_paddle_2

def winner():
    if ball.x + BALL_RADIUS > paddle_2.x and not hits_paddle(ball):
        return 1
    elif ball.x - BALL_RADIUS < paddle_1.x and not hits_paddle(ball):
        return 2
    else:
        return 0

def game_over():
    return winner() > 0


def draw():
    clear()

    # draw the table
    color(COLOR)
    width(5)
    line(0, -210, 0, 210)
    color(BG_COLOR)

    up()
    goto(0, 0)
    width(20)
    color(COLOR)
    circle(50)
    color(BG_COLOR)
    width(1)

    # draw the paddles
    rectangle(paddle_1.x, paddle_1.y, PADDLE_WIDTH, PADDLE_HEIGHT)
    rectangle(paddle_2.x, paddle_2.y, PADDLE_WIDTH, PADDLE_HEIGHT)

    # draw the ball
    color(COLOR)
    up()
    goto(ball.x, ball.y)
    dot(BALL_SIZE)
    color(BG_COLOR)
    update()


    # move the ball
    if not game_over():
        if hits_wall(ball):
            ball_aim.y = -ball_aim.y
        if hits_paddle(ball):
            ball_aim.x = -ball_aim.x
            ball_aim.__imul__(1.05)
        ball.move(ball_aim)
    else:
        print('Game Over. Winner: Player {}'.format(winner()))
        return

    ontimer(draw, 20)

def move_up(paddle):
    if paddle.y + PADDLE_HEIGHT <= 200:
        paddle.move(Vector(0, 5))

def move_down(paddle):
    if paddle.y >= -200:
        paddle.move(Vector(0, -5))

setup(420, 420, 0, 0)
hideturtle()
tracer(False)
bgcolor(BG_COLOR)
draw()
listen()
onkeypress(lambda :move_up(paddle_1), 'w')
onkeypress(lambda :move_down(paddle_1), 's')
onkeypress(lambda :move_up(paddle_2), 'Up')
onkeypress(lambda :move_down(paddle_2), 'Down')
done()