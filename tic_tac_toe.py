from turtle import *
from base import line
from math import floor

state = {'player': 1}
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def draw():
    clear()

    # Draw the board
    line(-60, -180, -60, 180)
    line(60, -180, 60, 180)
    line(-180, 60, 180, 60)
    line(-180, -60, 180, -60)

    # Draw the chips
    for i in range(3):
        for j in range(3):
            x, y = lower_left_coord(i, j)
            if grid[i][j] == 1:
                cross(x, y)
            elif grid[i][j] == 2:
                up()
                goto(x + 60, y + 10)
                down()
                color('red')
                width(5)
                circle(50)
                color('black')
                width(1)
    update()

    if game_over():
        winner_ = winner()
        if winner_ in [1, 2]:
            print('Game Over, winner is player ' + str(winner()))
        else:
            print('Game Over, Draw.')

def in_bounds(x, y):
    return -180 <= x <= 180 and -180 <= y <= 180

def cross(x, y, size = 120):
    color('blue')
    width(5)
    line(x + 10, y + 10, x + size - 10, y + size - 10)
    line(x + 10, y + size - 10, x + size - 10, y + 10)
    color('black')
    width(1)


def coord_to_idx(x, y):
    j = floor(x / 120 + 0.5) + 1
    i = 1 - floor(y / 120 + 0.5)
    return i, j

def lower_left_coord(i, j):
    x = 120 * j - 180
    y = -120 * i + 60
    return x, y

def game_over():
    return winner() > 0

def winner():
    # Check rows:
    for row in grid:
        if all(row[i] == 1 for i in range(3)):
            return 1
        if all(row[i] == 2 for i in range(3)):
            return 2

    # Check columns
    for j in range(3):
        if all(grid[i][j] == 1 for i in range(3)):
            return 1
        if all(grid[i][j] == 2 for i in range(3)):
            return 2

    # Check main diagonal
    if all(grid[i][i] == 1 for i in range(3)):
        return 1
    if all(grid[i][i] == 2 for i in range(3)):
        return 2

    # Check second diagonal
    if all(grid[i][2 - i] == 1 for i in range(3)):
        return 1
    if all(grid[i][2 - i] == 2 for i in range(3)):
        return 2

    # Check draw
    if any(grid[i][j] == 0 for i in range(3) for j in range(3)):
        return 0
    return 3

def place_chip(x, y):
    if game_over():
        return
    if in_bounds(x, y):
        # get corresponding coordinates
        i, j = coord_to_idx(x, y)
        # place the chip
        if grid[i][j] == 0:
            grid[i][j] = state['player']
            state['player'] = 1 if state['player'] == 2 else 2
            draw()

setup(405, 400, 0, 0)
hideturtle()
tracer(False)
draw()
getscreen().onclick(place_chip)
done()
