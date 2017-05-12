# -*- coding: utf-8 -*-
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

l=[('dm','123'),('gy','456')]
for name,pwd in l:
    register(name,pwd)

print(db)


