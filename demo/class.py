#!usr/bin/env python3
# -*- coding:utf-8 -*-

from enum import Enum

# Class 与 Instance
class Student(object):

    def __init__(self, **kw):
        print(kw)
        for k, v in kw.items():
            self.k = v
    
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

    def printInfo(self):
        for k, v in self.items():
            print(k, v)

dic = {
    "name": "neil",
    "age": 22,
    "score": 88
}
s1 = Student(**dic)

# 私有属性
class Worker(object):
    
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.__salary = salary  # 属性前加两个下划线为私有属性，外部不能访问
    
    def printInfo(self):
        print("%s is %s years old, %s's salary is %s" % (self.name,self.age,self.name,self.__salary))

    def set_salary(self,salary):
        if int(salary) > 0:
            self.__salary = salary
        else:
            raise ValueError('inviald salary')

w1 = Worker('James',25,13500)
w1.printInfo()

# 继承和多态
class Animal(object):
    def run(self):
        print('animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

d = Dog()
d.run()
print(type(d)=='object')
print(isinstance(d,Animal))
print(dir(d))

class Slot(object):
    __slots__ = ('name','age') # 用tuple定义允许绑定的属性名称
    pass

# Slot 的实例只能添加 name 和 age 两个属性

class Stu(object):
    def __init__(self, name, age, score):
        self.name = name
        self.__age = age
        self.__score = score
    
    @property
    def age(self):
        return self.__age

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if(score > 0 and score < 120):
            self.__score = score
        else:
            raise ValueError('inviald salary')

stu = Stu('neil',22,78)
stu.name = 'jack'
stu.score = 80
print(stu.name)
print(stu.age)
print(stu.score)

# 多重继承
class Bird(object):
    def fly(self):
        print('I can fly')

class RunableMixin(object):
    def run(self):
        print('I can run')

class Ostrich(Bird, RunableMixin):
    def all_i_can(self):
        self.fly()
        self.run()
ostrich = Ostrich()
ostrich.all_i_can()

# 定制类
# __getattr__
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
class Chain(object):
    def __init__(self, path=''):
        self.__path = path
    
    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path
    __repr__ = __str__

    def __call__(self, path):
        return Chain('%s:%s' % (self.__path, path))

print(Chain().users('michael').group('student').repos)

# 枚举类 Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3
    yellow = 4
    orange = 5
    black = 6
    red_alias = 1

blue = Color.blue
print(blue.name)
print(blue.value)

for c in Color:
    print(c.name, c.value)

# 如果想把值重复的成员也遍历出来，要用枚举的一个特殊属性__members__
for name, member in Color.__members__.items():
    print(name, member.value)

# 使用 type() 函数创建 class
def fn(self, name = 'world'):
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello()