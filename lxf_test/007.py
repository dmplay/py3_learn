# -*- coding: utf-8 -*-
import os
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])

L=[m + n for m in 'ABC' for n in 'XYZ']
print(L)

L=[d for d in os.listdir('F:/dmplay/')]
print(L)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)
    
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L=[k + '=' + v for k, v in d.items()]
print(L)

L = ['Hello', 'World', 'IBM', 'Apple']
L=[s.lower() for s in L]
print(L)

L = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L if(isinstance(s,str))]
print(L2)
