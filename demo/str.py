#!/usr/bin/env python3
# -*- coding:utf-8 -*-

str = 'this is demo string'
li = ('this','is','demo','string')
# 关于字符串的函数
print(ord('s'))
print(chr(98))
print(len(str))

# 字符串方法
print(str.count('s'))
print(str.find('is'))
print(str.replace('is', 'was')) # 返回一个新字符串，原字符串不改变
print(str.split(' '))
print(' '.join(li))
upper_str = str.upper()
print(upper_str)
print(upper_str.lower())

# 占位符
today = 'today is %s-%s-%s' % ('2017', '07', '05') 
print(today)