#encoding: utf-8

x = 1
y = 1

while x <= 20:
    while y <= 33:
        z = 100 - (x + y)
        if (z % 3 == 0) and (x * 5 + y * 3 + z / 3 == 100):
            print("����Ϊ%dֻ��ĸ��Ϊ%dֻ��С��Ϊ%dֻ" % (x, y, z))
        y += 1
    y = 1
    x += 1