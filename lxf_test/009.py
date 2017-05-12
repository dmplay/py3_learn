# -*- coding: utf-8 -*-
from functools import reduce

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

def normalize(name):
    return name[0].upper()+name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
     return reduce(lambda x, y: x*y,L)
    
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def str2float(s):
    index=s.find('.')
    return reduce(lambda x, y: x*10+y,map(char2num,s[:index]))+reduce(lambda x, y: x*0.1+y, map(char2num,reversed(s[s.find('.') + 1:])))*0.1
print('str2float(\'123.456\') =', str2float('123.456'))

