from random import *
from turtle import *
from base import Vector, square

LENGTH = 200
WIDTH = 200
snake = []
SIZE = 10
food = None

def food_in_wrong_place(food):
    for body in snake:
        if body.x == food.x and body.y == food.y:
            return True
    return False

def create_food():
    while True:
        x = randrange(-(LENGTH - SIZE), (LENGTH - SIZE), SIZE)
        y = randrange(-(WIDTH - SIZE), (WIDTH - SIZE), SIZE)
        food = Vector(x, y)
        if not food_in_wrong_place(food) and in_bounds(food):
            break
    return Vector(x, y)


def in_bounds(head):
    return -(LENGTH - SIZE) <= head.x <= (LENGTH - 2 * SIZE) and -(LENGTH - SIZE) <= head.y <= (LENGTH - 2 * SIZE)

def eats_itself():
    if len(snake) < 2:
        return False
    head = snake[0]
    for i in range(1, len(snake)):
        if head == snake[i]:
            return True
    return False

def eats_food(food):
    return snake[0] == food

def game_over():
    return not in_bounds(snake[0]) or eats_itself()

def add_body():
    last_body = snake[-1]
    if direction == 'U':
        new_body = Vector(last_body.x, last_body.y - SIZE)
    elif direction == 'D':
        new_body = Vector(last_body.x, last_body.y + SIZE)
    elif direction == 'L':
        new_body = Vector(last_body.x + SIZE, last_body.y)
    else:
        new_body = Vector(last_body.x - SIZE, last_body.y)
    snake.append(new_body)

direction = 'U'

def move():
    global food
    head = snake[0]
    if eats_itself():
        square(head.x, head.y, SIZE, 'red')
        print('Game over')
        return
    if not in_bounds(head):
        print('Game over')
        return
    clear()
    if eats_food(food):
        # Add food to the snake body
        add_body()
        # create new food
        food = create_food()

    # display the food
    square(food.x, food.y, SIZE, 'blue')

    # display the moved snake
    if direction == 'U':
        new_head = Vector(head.x, head.y + SIZE)
    elif direction == 'D':
        new_head = Vector(head.x, head.y - SIZE)
    elif direction == 'L':
        new_head = Vector(head.x - SIZE, head.y)
    else:
        new_head = Vector(head.x + SIZE, head.y)
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]
    snake[0] = new_head

    for body in snake:
        square(body.x, body.y, SIZE, 'white')

    ontimer(move, 50)

def create_head_and_food():
    x = randrange(-LENGTH // 2, LENGTH // 2, SIZE)
    y = randrange(-LENGTH // 2, LENGTH // 2, SIZE)
    head = Vector(x, y)
    snake.append(head)
    print(head)

    global food
    food = create_food()

    move()

def direction_up():
    global direction
    direction = 'U'

def direction_down():
    global direction
    direction = 'D'

def direction_left():
    global direction
    direction = 'L'

def direction_right():
    global direction
    direction = 'R'

setup(2 * LENGTH + 20, 2 * WIDTH + 20, 0, 0)
bgcolor('black')
hideturtle()
tracer(False)
create_head_and_food()
onkeypress(direction_up, 'Up')
onkeypress(direction_down, 'Down')
onkeypress(direction_left, 'Left')
onkeypress(direction_right, 'Right')
getscreen().listen()
done()


