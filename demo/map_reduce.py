#!usr/bin/env python3
# -*- coding:utf-8 -*-
from functools import reduce

# map
List = map(lambda x: x * 2, [1,2,3,4,5,6]) 
print(list(List))

# filter
odd = filter(lambda x: x % 2 == 0, [1,2,3,4,5,6])
print(list(odd))
# map 和 filter 返回的都是一个Interator对象

# reduce  reduce需要从functools中进行导入
total = reduce(lambda x, y: x + y, [1,2,3,4,5,6])  # reduce 直接返回结果
print(total)

# sorted
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

sortByName = sorted(L, key = lambda t: t[0])
sortByScore = sorted(L, key = lambda t: t[1])
sortByScoreASC = sorted(L, key = lambda t: t[1], reverse = True)
print(sortByName)
print(sortByScore)
print(sortByScoreASC)