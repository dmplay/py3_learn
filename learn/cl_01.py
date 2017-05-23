# !/usr/bin/python
# -*- coding: UTF-8 -*-

def show():
    list_num = [1, 2, 3, 4]
    list = [i * 100 + j * 10 + k for i in list_num for j in list_num for k in list_num if
            (j != i and k != j and k != i)]
    print(list)

if __name__=='__main__':
    show()
