# -*- coding: utf-8 -*-

def readFile():
    with open('F:/dmplay/python3/020.py', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print(line) # 把末尾的'\n'删掉 .strip()

def writeFile():
    with open('F:/dmplay/python3/test.txt', 'w',encoding='utf-8') as f:
        f.write('Hello, world!')


if __name__ == '__main__':
    writeFile()



