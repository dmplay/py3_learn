# !/usr/bin/python
# -*- coding: UTF-8 -*-
import requests,os
os.chdir('D:\\dmplay\\test')
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

res = requests.get('http://www.baidu.com')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()