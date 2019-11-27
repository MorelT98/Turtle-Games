from turtle import *
from random import randrange
from base import square, Vector

# variable
food = Vector(0, 0)
snake = [Vector(10, 0)]
aim = Vector(0, -10)

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    # move snake one segment forward
    head = snake[-1].copy()
    head.move(aim)
    # If the snake is out of bounds, or eats itself
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    # Add new head to snake
    snake.append(head)

    if head == food:
        # if snake eats the food
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        # Remove last body of the snake
        snake.pop(0)

    clear()
    for body in snake:
        square(body.x, body.y, 9, 'white', 'white')
    square(food.x, food.y, 9, 'green', 'white')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
bgcolor('black')
hideturtle()
tracer(False)
listen()
onkey(lambda : change(10, 0), 'Right')
onkey(lambda : change(-10, 0), 'Left')
onkey(lambda : change(0, 10), 'Up')
onkey(lambda : change(0, -10), 'Down')

move()
done()
