#!usr/bin/env python3
# -*- coding:utf-8 -*-

# if else
age = 18
if age < 16 :
    print('litter boy')
elif age < 25 :
    print('young man')
else:
    print('lol')


# 循环

# for ... in
names = ['neil', 'jack', 'jolin']
for name in names:
    print(name)

total = 0
for num in range(101):
    total += num
print(total)

# while 
n = 99
while n > 0:
    n -= 2
    if n < 10:
        break
print(n)

m = 99
while m > 0:
    m -= 1
    if m % 2 == 1:
        continue
    print(m)
