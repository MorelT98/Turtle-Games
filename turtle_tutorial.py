import turtle
import math

keith = turtle.Turtle()

########################################################
##      1 - TURTLE BASICS: DRAW TWO SQUARES           ##
########################################################

# keith.forward(100)
# keith.left(45)
# keith.forward(100)
# keith.right(90)
# keith.forward(100)

# keith.color('blue', 'cyan')
#
# keith.begin_fill()
# keith.forward(100)
# keith.left(90)
# keith.forward(100)
# keith.left(90)
# keith.forward(100)
# keith.left(90)
# keith.forward(100)
#
# keith.penup()
# keith.forward(10)
# keith.pendown()
#
# keith.forward(100)
# keith.left(90)
# keith.forward(100)
# keith.left(90)
# keith.forward(100)
# keith.left(90)
# keith.forward(100)
#
# keith.end_fill()

########################################################
##               2 - DRAW A FLOWER                    ##
########################################################
#
# keith.color('red', 'yellow')
# keith.speed(1000)
#
# keith.begin_fill()
# for i in range(2000):
#     keith.forward(10)
#     keith.left(math.sin(i / 10) * 25)
# keith.end_fill()

########################################################
##         3 - DRAW STARS USING RECURSION             ##
########################################################

# keith.getscreen().bgcolor('#994444')
# keith.speed(20)
#
# def star(length):
#     if length < 20:
#         return
#     for i in range(5):
#         keith.forward(length)
#         keith.left(216)
#         star(length / 4)
#
# star(400)


angle = math.atan((210 + 100) / (210 - 100)) * 180 / math.pi
keith.penup()
keith.goto(-210, -210)
keith.pendown()
keith.left(angle)
while True:
    keith.forward(20)
    keith.right(20)
    if keith.ycor() < -210:
        break

turtle.done()