#!usr/bin/env python3
# -*- coding:utf-8 -*-

# list
l = ['this','is','demo','of','list']

# 获取list中元素
print(len(l))
print(l[0])     # 列表第一个元素
print(l[-1])    # 列表最后一个元素
print(l[2:])    # 列表第三到最后一个元素
print(l[:2])    # 列表前两个元素
print(l[1:4])   # 列表第二到第四个元素

# 操作list
print(l.append('last'))     # 返回None，改变了原列表
print(l.insert(1,'was'))    # 同append
print(l.pop(1))              # 返回被删除的元素，改变了原列表
print(l)

# tuple

t = ('this','is','demo','of','tuple')

# 获取tuple中元素
print(len(t))
print(t[0])     # 元组第一个元素
print(t[-1])    # 元组最后一个元素
print(t[2:])    # 元组第三到最后一个元素
print(t[:2])    # 元组前两个元素
print(t[1:4])   # 元组第二到第四个元素

# 只有1个元素的tuple定义时必须加一个逗号,以免误解成数学计算意义上的括号
one_tuple = (1,)
print(one_tuple)