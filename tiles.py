from random import shuffle
from turtle import *

SIZE = 100
over = False

class Tile():
    def __init__(self, value):
        self.value = value


tiles = [Tile(i) for i in range(16)]
shuffle(tiles)

def find(value):
    for i in range(16):
        if tiles[i].value == value:
            return i
    return -1

def are_sorted(values):
    current = float('-inf')
    for i in range(len(values)):
        if current > values[i]:
            return False
        current = values[i]
    return True

def idx_to_coord(idx):
    x = 100 * (idx % 4) - 200
    y = -100 * (idx // 4) + 100
    return x, y

def coord_to_idx(x, y):
    x = (x // 100) * 100
    y = (y // 100) * 100
    idx = 4 * (y - 100) / (-100) + (x + 200) / 100
    return int(idx)

def in_bounds(x, y):
    return -200 <= x <= 200 and -200 <= y <= 200

def game_over():
    values = [tile.value for tile in tiles]
    idx_zero = find(0)
    if idx_zero == 0:
        if are_sorted(values):
            return True
    elif idx_zero == 15:
        values.remove(0)
        if are_sorted(values):
            return True
    return False

def square(idx, size, color1, color2):
    # Get the text
    if tiles[idx].value == 0:
        text = ''
    else:
        text = str(tiles[idx].value)

    # Draw the square
    color(color1, color2)
    width(4)
    x, y = idx_to_coord(idx)
    up()
    goto(x, y)
    down()
    begin_fill()
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()

    # Write the message
    up()
    if tiles[idx].value < 10:
        goto(x + 40, y + 30)
    else:
        goto(x + 30, y + 30)
    write(text, font=('Arial', 30, 'bold'))
    width(1)

def draw():
    clear()
    # draw the tiles
    for idx in range(16):
        square(idx, SIZE, 'black', 'white')

    # Check if the tiles are not sorted already
    over = game_over()
    if over:
        print('Congratulations!')
        return

# Returns the neighbors of a given tile
def get_neighbors(idx):
    neighbors = [idx - 1, idx + 1, idx - 4, idx + 4]
    # Remove left neighbor if we are on the left edge
    if idx % 4 == 0:
        neighbors.remove(idx - 1)
    # Remove right neighbor if we are on the right edge
    if (idx + 1) % 4 == 0:
        neighbors.remove(idx + 1)
    # Remove top neighbor if we are on the top edge
    if idx < 4:
        neighbors.remove(idx - 4)
    # Remove bottom neighbor if we are on the bottom edge
    if idx > 11:
        neighbors.remove(idx + 4)
    return neighbors

# Checks if two tiles are neighbors, given their indices
def are_neighbors(idx1, idx2):
    return idx1 in get_neighbors(idx2)

# swaps two tiles
def swap(idx1, idx2):
    temp = tiles[idx1]
    tiles[idx1] = tiles[idx2]
    tiles[idx2] = temp

# Move the clicked tile
def move(x, y):
    if game_over():
        return
    if in_bounds(x, y):
        idx = coord_to_idx(x, y)
        # find the empty tile
        idx_empty = -1
        for i in range(16):
            if tiles[i].value == 0:
                idx_empty = i
                break
        # If the empty tile and current tile are neighbors, swap them
        if are_neighbors(idx, idx_empty):
            swap(idx, idx_empty)
            square(idx, SIZE, 'black', 'white')
            square(idx_empty, SIZE, 'black', 'white')
            if game_over():
                print('Congratulations!')


setup(420, 420, 0, 0)

hideturtle()
tracer(False)
draw()
listen()
onscreenclick(move)
done()
