# !/usr/bin/python
# -*- coding: UTF-8 -*-
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

for k,v in count.items():
    print(k+":"+str(v))

pprint.pprint(count)