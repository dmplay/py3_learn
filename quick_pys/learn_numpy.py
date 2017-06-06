import numpy as np
import time
import math
import numpy as np


def showArray():
    a = np.array([1, 2, 3, 4])
    b = np.array((5, 6, 7, 8))
    c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
    print(c.dtype)
    print(a.shape)
    print(c.shape)
    print(c)
    c.shape = 4,3 #shape=形状 行,列
    print(c)
    c.shape = 2,-1
    print(c)
    d = a.reshape((2,2))
    print(d)
    a[1]=100
    print(d)
    e=np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]], dtype=np.float)
    print(e)
    f=np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]], dtype=np.complex)
    print(f)


def showRange():
    a = np.arange(0, 1, 0.1) #等差
    print(a)
    a = np.linspace(0, 1, 12) #等分
    print(a)
    a = np.logspace(0, 2, 20) #等比
    print(a)


def showBytes():
    s = "abcdefgh"
    # Python的字符串实际上是字节序列，每个字符占一个字节，因此如果从字符串s创建一个8bit的整数数组的话，
    # 所得到的数组正好就是字符串中每个字符的ASCII编码
    a = np.fromstring(s, dtype=np.int8)
    print(a)
    # 字符串s创建16bit的整数数组，那么两个相邻的字节就表示一个整数，
    # 把字节98和字节97当作一个16位的整数，它的值就是98*256+97 = 25185。
    # 可以看出内存中是以little endian(低位字节在前)方式保存数据的
    a = np.fromstring(s, dtype=np.int16)
    print(a)
    # 把整个字符串转换为一个64位的双精度浮点数数组
    a = np.fromstring(s, dtype=np.float)
    print(a)


def showFunction():
    a = np.fromfunction(func, (10,))
    print(a)
    a = np.fromfunction(func2, (9, 9))
    print(a)

def func(i):
    return i % 4 + 1


def func2(i, j):
    return (i+1) * (j+1)


def showSavePut():
    a = np.arange(10)
    print(a[5])
    x = np.arange(10, 1, -1)
    print(x[[3, 3, 1, 8]])
    b = x[np.array([3, 3, -3, 8])]
    b[2] = 100
    print(b)
    print(x)
    x[[3, 5, 1]] = -1, -2, -3
    print(x)


def showBooleanArray():
    x = np.arange(5, 0, -1)
    a = x[np.array([True, False, True, False, False])]
    print(a)
    a = x[[True, False, True, False, False]]
    print(a)
    a = x[np.array([True, False, True, True])]
    print(a)
    x[np.array([True, False, True, True])] = -1, -2, -3
    print(x)
    x = np.random.rand(10)
    a = x > 0.5
    print(a)
    print(x[x > 0.5])


def makeArray():
    a = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
    print(a)


def showMath():
    x = [i * 0.001 for i in range(1000000)]
    start = time.clock()
    for i, t in enumerate(x):
        x[i] = math.sin(t)
    print("math.sin:", time.clock() - start)

    x = [i * 0.001 for i in range(1000000)]
    x = np.array(x)
    start = time.clock()
    np.sin(x, x)
    print("numpy.sin:", time.clock() - start)


def triangle_wave1(x, c, c0, hc):
    x = x - int(x) # 三角波的周期为1，因此只取x坐标的小数部分进行计算
    if x >= c: r = 0.0
    elif x < c0: r = x / c0 * hc
    else: r = (c-x) / (c-c0) * hc
    return r

def triangle_func(c, c0, hc):
    def trifunc(x):
        x = x - int(x) # 三角波的周期为1，因此只取x坐标的小数部分进行计算
        if x >= c: r = 0.0
        elif x < c0: r = x / c0 * hc
        else: r = (c-x) / (c-c0) * hc
        return r

    # 用trifunc函数创建一个ufunc函数，可以直接对数组进行计算, 不过通过此函数
    # 计算得到的是一个Object数组，需要进行类型转换
    return np.frompyfunc(trifunc, 1, 1)

def showBroadcast():
    a = np.arange(0, 60, 10).reshape(-1, 1)
    b = np.arange(0, 5)
    c = a + b
    print(c)
    x, y = np.ogrid[0:5, 0:5]
    print(x)
    print(y)


def showReduceAndOr():
    a = np.add.reduce([1, 2, 3])  # 1 + 2 + 3
    print(a)
    a = np.add.reduce([[1, 2, 3], [4, 5, 6]], axis=1)  # 1,4 + 2,5 + 3,6
    print(a)
    a = np.add.accumulate([1, 2, 3])
    print(a)
    a = np.add.accumulate([[1, 2, 3], [4, 5, 6]], axis=1)
    print(a)
    a = np.array([1, 2, 3, 4])

    '''
    if indices[i] < indices[i+1]:
        result[i] = np.reduce(a[indices[i]:indices[i+1]])
    else:
        result[i] = a[indices[i]
    '''
    result = np.add.reduceat(a, indices=[0, 1, 0, 2, 0, 3, 0])
    print(result)
    a = np.multiply.outer([1,2,3,4,5],[2,3,4])
    print(a)


def showFile():
    a = np.arange(0, 12)
    a.shape = 3, 4
    print(a.dtype)
    print(a)
    a.tofile("a.bin")
    b = np.fromfile("a.bin", dtype=np.float)
    print(b)
    print(b.dtype)
    b = np.fromfile("a.bin", dtype=np.int32)
    print(b)
    b.shape = 3, 4
    print(b)
    np.save("a.npy", a)
    c = np.load("a.npy")
    print(c)
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.arange(0, 1.0, 0.1)
    c = np.sin(b)
    np.savez("result.npz", a, b, sin_array=c)
    r = np.load("result.npz")
    print(r["arr_0"])

if __name__ == "__main__":
    showFile()
