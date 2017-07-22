#!usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import json

# 读文件
# read
try:
    f = open('class.py','r')
    print(f.read())
except IOError as e:
    print(e)
finally:
    f.close()

# readline 读取第一行
try:
    rline = open('class.py','r')
    for line in rline.readline():
        print(line.strip()) # 去掉末尾的 \n
except IOError as e:
    print(e)
finally:
    f.close()

# readlines 读取全部内容
try:
    rline = open('class.py','r')
    for line in rline.readlines():
        print(line.strip()) # 去掉末尾的 \n
except IOError as e:
    print(e)
finally:
    f.close()

try:
    w = open('input.txt', 'w', errors="ignore")
    w.write('测试文件写入')
except IOError as e:
    print(e)
finally:
    w.close()

try:
    w = open('input.txt', 'a', errors="ignore") # 追加
    w.write('测试文件写入')
except IOError as e:
    print(e)
finally:
    w.close()

# os模块
dirname = os.path.abspath('.')
print(os.path.split(dirname))
testdir = os.path.join(dirname,'test')
os.mkdir(testdir)
newdir = os.path.join(dirname,'new')
os.rename(testdir,newdir)
os.rmdir(newdir)
os.rename('input.txt','newInput.txt')
os.remove('newInput.txt')
print(os.path.isdir(dirname))
print(os.path.isabs('class.py'))
print(os.path.isfile('class.py'))

d = {
    "name": "neilLin",
    "age": 23,
    "job": "Diver"
}
stringify = json.dumps(d)
print(stringify)
writeJson = open('json.json','w')
json.dump(d, writeJson)
writeJson.close()
print(json.loads(stringify))
parseJson = open('json.json','r')
p = json.load(parseJson)
print(p)
parseJson.close()