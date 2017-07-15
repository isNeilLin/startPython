#!usr/bin/env python3
# -*- coding:utf-8 -*-

# Class 与 Instance
class Student(object):

    def __init__(self, **kw):
        print(kw)
        for k, v in kw.items():
            self.k = v
    
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