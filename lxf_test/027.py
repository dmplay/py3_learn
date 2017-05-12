# -*- coding: utf-8 -*-
import os

os.path.abspath('.')

f=os.path.join(os.path.abspath('.'), 'testdir')
os.mkdir(f)
os.rmdir(f)
os.path.split(f)
os.path.splitext(f)

def searchFiles(path,words):
    for x in os.listdir(path) :
        fullPath=os.path.join(path,x)
        if os.path.isdir(fullPath):
            searchFiles(fullPath,words)
        else:
            searchWords(fullPath,words)

def searchWords(filePath,words):
     with open(filePath, 'r', encoding='utf-8') as f:
        if f.read().find(words)>0:
            print(filePath)
        
searchFiles('.','dmplay');
