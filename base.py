import collections
import math
import turtle
import os

def floor(value, size, offset = 200):
    return float(((value + offset) // size) * size - offset)

def path(filename):
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    fullpath = os.path.join(dirpath, filename)
    return fullpath

def line(a, b, x, y):
    turtle.up()
    turtle.goto(a, b)
    turtle.down()
    turtle.goto(x, y)

def square(x, y, size, color1, color2, turtle=turtle):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color1, color2)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


class Vector(collections.Sequence):
    PRECISION = 6
    __slots__ = ('_x', '_y', '_hash')


    def __init__(self, x, y):
        self._hash = None
        self._x = round(x, self.PRECISION)
        self._y = round(y, self.PRECISION)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if self._hash is not None:
            raise ValueError('Cannot set x after hashing')
        self._x = round(value, self.PRECISION)

    @ property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if self._hash is not None:
            raise ValueError('Cannot set y after hashing')
        self._y = round(value, self.PRECISION)


    def __hash__(self):
        #v.__hash__() -> hash(v)
        if self._hash is None:
            pair = (self.x, self.y)
            self._hash = hash(pair)

        return self._hash

    def __len__(self):
        return 2

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        else:
            raise IndexError

    def copy(self):
        type_self = type(self)
        return type_self(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self._x == other._x and self._y == other._y
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Vector):
            return self.x != other.x or self.y != other.y
        return NotImplemented

    def __iadd__(self, other):
        if self._hash is not None:
            raise ValueError("Cannot add vector after hashing")
        if isinstance(other, Vector):
            self._x += other.x
            self._y += other.y
        else:
            self._x += other
            self._y += other
        return self

    def __add__(self, other):
        copy = self.copy()
        return copy.__iadd__(other)

    __radd__ = __add__

    def move(self, other):
        self.__iadd__(other)

    def __isub__(self, other):
        if self._hash is not None:
            raise ValueError("Cannot subtract vector after hashing")
        if isinstance(other, Vector):
            self._x -= other.x
            self._y -= other.y
        else:
            self._x -= other
            self._y -= other
        return self

    def __sub__(self, other):
        copy = self.copy()
        return copy.__isub__(other)

    def __imul__(self, other):
        if self._hash is not None:
            raise ValueError("Cannot multiply vector after hashing")
        if isinstance(other, Vector):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        return self

    def __mul__(self, other):
        copy = self.copy()
        return copy.__imul__(other)

    def scale(self, other):
        self.__imul__(other)

    def __itruediv__(self, other):
        if self._hash is not None:
            raise ValueError("Cannot divide vector after hashing")
        if isinstance(other, Vector):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.y /= other
        self.x = round(self.x, self.PRECISION)
        self.y = round(self.y, self.PRECISION)
        return self

    def __truediv__(self, other):
        copy = self.copy()
        return copy.__itruediv__(other)

    def __neg__(self):
        return self.__mul__(-1)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def rotate(self, angle):
        if self._hash is not None:
            raise ValueError('Cannot rotate vector after hashing')
        angle = angle * math.pi / 180
        cos = math.cos(angle)
        sin = math.sin(angle)
        x = self.x
        y = self.y
        self.x = x * cos - y * sin
        self.y = y * cos + x * sin
        return self

    def __repr__(self):
        type_self = type(self)
        name = type_self.__name__
        return '{} ({}, {})'.format(name, self.x, self.y)

