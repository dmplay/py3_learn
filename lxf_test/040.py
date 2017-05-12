# -*- coding: utf-8 -*-
import itertools

ns = itertools.repeat('A', 3)
for n in ns:
     print(n)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)

print(list(ns))

for key, group in itertools.groupby('AaAbBBCcAAA',lambda c: c.upper()):
    print(key, list(group))
