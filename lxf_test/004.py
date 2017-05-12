# -*- coding: utf-8 -*-
import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def nop():
    if age >= 18:
        pass

print(my_abs(2))

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

def quadratic(a, b, c):
    return ((-b)+math.sqrt(b*b-4*a*c))/(2*a),((-b)-math.sqrt(b*b-4*a*c))/(2*a)

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
