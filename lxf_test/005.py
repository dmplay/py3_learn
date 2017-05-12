# -*- coding: utf-8 -*-
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

y=power(5,3)
print(y)

y=power(5)
print(y)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

y=calc(1, 2, 3)
print(y)
nums = [1, 2, 3,4,5]
y=calc(*nums)
print(y)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
