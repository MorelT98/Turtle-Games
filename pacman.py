from random import choice
from turtle import *
from base import Vector, floor

state = {'score': 0}    # keeps track of the score
path = Turtle(visible=False)    # draws the path
writer = Turtle(visible=False)  # shows the score

aim = Vector(5, 0)  # Initial direction of the pacman player (to the right)
pacman = Vector(-40, -80)

# 4 ghosts, their starting location and starting direction
ghosts = [
    [Vector(-180, 160), Vector(5, 0)],
    [Vector(-180, -160), Vector(0, 5)],
    [Vector(100, 160), Vector(0, -5)],
    [Vector(100, -160), Vector(-5, 0)]
]

# 1 = blue square
# 0 = black square
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    # drawing square with x and y
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
    for count in range(4):
        path.forward(20)
        path.left(90)
    path.end_fill()

# Get the corresponding index in the tiles, given the point
def offset(point):
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# Check if a given point is valid, which is, not in a wall
# and has coordinates that are multiples of 20 (its size)
def valid(point):
    # get corresponding index in tiles
    index = offset(point)
    # if the tile at that point is a wall
    if tiles[index] == 0:
        return False
    # Check the opposite corner of the tile as well, to prevent that
    #   corner from going into a wall
    index = offset(point + 19)
    if tiles[index] == 0:
        return False
    return point.x % 20 == 0 or point.y % 20 == 0

# Draw the pacman environment
def world():
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]
        if tile > 0:
            # Get the corresponding coordinates (lower left corner of the square)
            # for each tile
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
            # If the tile is a path, draw food on its center
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


# Draws and updates the moving parts of the game: pacman, ghosts, score
def move():
    # update score
    writer.undo()   # erase previous score first
    writer.write(state['score'])
    clear()

    # move pacman
    if valid(pacman + aim):
        pacman.move(aim)
    # Get pacman index in tiles
    index = offset(pacman)
    if tiles[index] == 1:
        # Change the tile number so that we know there's no food there,
        # but DO NOT change it to zero, since zero is used for walls
        tiles[index] = 2
        state['score'] += 1     # update score
        # Get the corresponding (x, y) coordinate, then redraw an empty blue square (with no food)
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)
    # draw pacman
    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    # move and draw ghosts
    for point, course in ghosts:
        # If ghost is not hitting a wall
        if valid(point + course):
            point.move(course)
        else:
            # If it hits a wall, change its direction randomly
            options = [
                Vector(5, 0),
                Vector(-5, 0),
                Vector(0, 5),
                Vector(0, -5)
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y
        # draw ghost
        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')
    update()

    # If a ghost touches pacman, end the game
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 30)

def change(x, y):
    # change pacman's aim if valid
    if valid(pacman + Vector(x, y)):
        aim.x = x
        aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda : change(5, 0), 'Right')
onkey(lambda : change(-5, 0), 'Left')
onkey(lambda : change(0, -5), 'Down')
onkey(lambda : change(0, 5), 'Up')
world()
move()

done()