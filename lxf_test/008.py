# -*- coding: utf-8 -*-
g = (x * x for x in range(10))
for n in g:
     print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

def triangles():
    L1=[1]
    while True:
        yield L1
        L1=[L1[0]]+[(L1[i]+L1[i-1]) for i in range(1,len(L1))]+[L1[-1]]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
