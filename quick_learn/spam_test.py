# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所
有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入and。例如，将
前面的spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。但你的函数应
该能够处理传递给它的任何列表。
"""
import copy
spam = ['apples', 'bananas', 'tofu', 'cats']
spam = [23, 123, 'tofu', 'cats']
for x in range(len(spam)):
    bef = ""
    split = ", "
    if x == len(spam)-1:
        bef = "and "
        split = ""
    print(bef+str(spam[x]), end=split)
print()
spam1 = copy.copy(spam)
if len(spam1) > 1:
    spam1[-1] = "and " + str(spam1[-1])
print(', '.join([str(x) for x in spam1]))

print()

grid = [['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']]

index = 0
while True:
    count = 0
    for x in grid:
        if index < len(x):
            count = count+1
            print(x[index], end="")
    index = index+1
    if count == 0:
        break
    print()
