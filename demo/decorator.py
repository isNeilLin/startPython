#!usr/bin/env python3
# -*- coding:utf-8 -*-

import functools

def log(func):
    def wrapper(*args, **kw):
        print('function %s will be call' % func.__name__)
        return func(*args, **kw)
    return wrapper

"""
    由于 log() 是一个decorator，返回一个函数，所以原来的 now() 函数仍然存在，只是现在同名的 now
    变量指向了新的函数。于是调用 now 将执行新函数。即在 log() 中返回的 wrapper() 函数
"""

@log
def now():
    print('2017-07-12')

now()
print(now.__name__) # wrapper

"""
    如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数。比如要自定义log的文本
"""

def customLog(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s: ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@customLog('execute')
def test():
    print('2017-07-12')

test()
print(test.__name__) # wrapper

def newLog(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s will be call ' % func.__name__)
        return func(*args, **kw)
    return wrapper

@newLog
def today():
    print('2017-07-12')

today()
print(today.__name__) # today

# 偏函数
int2 = functools.partial(int,base=2)
print(int2('1000000'))