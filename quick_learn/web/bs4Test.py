# !/usr/bin/python
# -*- coding: UTF-8 -*-
import requests, bs4
res = requests.get('http://www.baidu.com')
res.raise_for_status()
exampleSoup = bs4.BeautifulSoup(res.text,"html.parser")
elems = exampleSoup.select('#lg')
print(len(elems))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)