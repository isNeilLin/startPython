# 迭代

from collections import Iterable

# 在Python中，迭代是通过for ... in来完成的
dic = {
    'name': 'neil',
    'age': 23,
    'city': 'beijing'
}

# 默认情况下，dict迭代的是key。
for k in dic:
    print(k)

# 如果要迭代value，可以用for value in d.values()
for v in dic.values():
    print(v)

# 如果要同时迭代key和value，可以用for k, v in d.items()。
for k, v in dic.items():
    print(k + ': ' + str(v))

# 通过collections模块的Iterable类型判断一个对象是不是可迭代
print(isinstance('this is a string', Iterable))

for i, v in enumerate(['A','B','C','D']):
    print(i, v)
