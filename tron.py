from turtle import *
from base import square, Vector

p1xy = Vector(-100, 0)
p1aim = Vector(4, 0)
p1body = set()

p2xy = Vector(100, 0)
p2aim = Vector(-4, 0)
p2body = set()

def inside(head):
    # return true if head is inside boundary
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    if not inside(p1head) or p1head in p2body:
        print('Player blue won')
        return

    if not inside(p2head) or p2head in p1body:
        print('Player red won')
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 50)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda : p1aim.rotate(90), 'a')
onkey(lambda : p1aim.rotate(-90), 'd')
onkey(lambda : p2aim.rotate(90), 'j')
onkey(lambda : p2aim.rotate(-90), 'l')
draw()
done()

