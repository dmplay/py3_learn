# -*- coding: utf-8 -*-
import re

def show():
    re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
    test = '用户输入的字符串'
    if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
        print('ok')
    else:
        print('failed')
    l=re.split(r'[\s\,\;]+', 'a,b;; c  d')
    print(l)
    l = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    print(l.group(1))

    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    l=re_telephone.match('010-12345').groups()
    print(l)
    l=re_telephone.match('010-8086').groups()
    print(l)

def testRe():
    re_email = re.compile(r'^(\w+)@(\w+)\.\w+$')
    l=re_email.match('someone@gmail.com').groups()
    print(l)

if __name__=='__main__':
    testRe()

