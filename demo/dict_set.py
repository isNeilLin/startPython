#!usr/bin/env python3
# -*- coding:utf-8 -*-

# dict
dic = {
    'neil': 23,
    'jack': 25,
    'joylin': 21
}
print(dic['neil'])
print(dic.get('n'))  # get方法取值，如果不存在返回None

print('tom' in dic)

dic.pop('joylin')   # 删除dict中的一个元素
items = dic.items() # 以列表返回可遍历的(键, 值) 元组数组
keys = dic.keys()   # 以列表返回一个字典所有的键
values = dic.values()   # 以列表返回字典中的所有值
print(items)
print(keys)
print(values)
dic.clear()     # 清空dict
print(dic)
dic.update({
    'newDic': 32
})
del dic
# print(dic)

# set

s1 = set(['neil','jack','joylin'])
s2 = set([])
s1.remove('jack')
s2.add('neil')
s2.add('tom')
print(s1)
print(s2)
print(s1 & s2)
print(s1 | s2)