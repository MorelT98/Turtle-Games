from turtle import *
from math import atan, pi, sqrt, cos, sin
t = 0
tstep = 4
delx = 5   # Uniform motion in x axis
g = -1  # fixed acceleration
yvel = 20   # initial vel in y
y = 0   # y position

# draw a cliff that the ball can be thrown from
penup()
goto(-100, 0)
pendown()
color('green')
forward(150)
right(90)
forward(100)
penup()
goto(0, 0)
pendown()
color('blue')

# print('run the simulation for 50 seconds')
# while t < 50:
#     t = t + tstep
#     x = t * delx
#     yvel = yvel + g * tstep
#     y = y + yvel * tstep
#     goto(x, y)
#     dot(2, 'blue')
# print('Final y position is {}m'.format(y))

def simulate(x, y):
    print('Simulating')
    t = 0
    tstep = 0.5
    g = -2
    x0 = 0
    y0 = 0
    angle = atan(y / x)
    v0 = sqrt(x ** 2 + y ** 2) / 10
    v0_x = v0 * cos(angle)
    v0_y = v0 * sin(angle)
    vx = v0_x
    vy = v0_y
    penup()
    goto(x0, y0)
    pendown()
    x = x0
    y = y0
    while t < 50:
        print(x, y)
        goto(x, y)
        x = t * vx
        vy = vy + g * tstep
        y = y + vy * tstep
        t = t + tstep
        dot(2, 'blue')

up()
onscreenclick(simulate)

done()
