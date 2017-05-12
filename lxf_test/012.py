# -*- coding: utf-8 -*-

def log(text='execute'):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            print('begin call')
            data=func(*args, **kw)
            print('end call')
            return data
        return wrapper
    return decorator

@log()
def now():
    print('2015-3-25')

@log('execute')
def how():
    print('2017-3-25')
