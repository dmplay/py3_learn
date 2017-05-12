# -*- coding: utf-8 -*-
import struct

def show():
    with open('F:/dmplay/python3/show.bmp','rb') as f:
        l=struct.unpack('<ccIIIIIIHH', f.read(30))
        print('图片大小:%s * %s ' % (l[6],l[7]))
        print('颜色数:%s ' % l[9])

show()
