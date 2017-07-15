#!usr/bin/env python3
# -*- coding:utf-8 -*-

# function
def my_abs(x):
    if x >=0:
        return x
    else:
        return -x

# 空函数
def empty():
    """ pass可以用来作为占位符，先放一个pass，让代码能运行起来。 """
    pass

# 返回多个值
def mulity(x,y):
    """ 函数返回多值其实就是返回一个tuple """
    x *= 2
    y += 3
    return x,y

# 默认参数 
def power(x, n=2):  
    """ 默认参数必须指向不变对象！ """
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 可变参数
def calc(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print(my_abs(-3))
print(mulity(4,8))
print(power(3,3))
# 如果利用可变参数，调用函数的方式可以简化成这样：
print(calc(2,4,5,6,8,9))

# 如果已经有一个list或者tuple，要调用一个可变参数:
# list或tuple前面加一个*号，可以把list或tuple的元素变成可变参数传进去
nums = [1,2,3,4,5,6,7,8,9]
print(calc(*nums))

# 关键字参数

def person(name, age, **kw):
    print('name: ', name, 'age: ', age, kw)

person('neil', 23, city="Beijing")
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('neil', 23, **extra)

# 命名关键字参数

def per(name, age, *, city, job):
    print(name, age, city, job)

per('neil', 23, city="beijing", job="Engineer")

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了

def per2(name, age, *nums, city, job):
    print(name,age,nums,city,job)

per2('neil', 23, *nums, city="beijing", job="Engineer")

# 递归函数

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(5))

# 匿名函数
lambda arg: arg + '1'  # Python匿名函数只支持一行表达式