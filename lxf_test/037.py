# -*- coding: utf-8 -*-
import base64

x=base64.b64encode(b'binary\x00string')
print(x)

x=base64.b64decode(x)
print(x)

x=base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(x)

x=base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(x)

x=base64.urlsafe_b64decode('abcd--__')
print(x)

def safe_base64_decode(s):
    for x in range(4-len(s)%4):
        s=s+'='
    print(s)

safe_base64_decode('YWJjZA')
