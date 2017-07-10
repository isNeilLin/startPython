# 廖雪峰python教程学习笔记

## 基础语法

#### 安装
- MAC下python安装 ： `brew install python3`
- Windows下安装 ：下载exe安装包，勾选 `Add Python 3.X to PATH`

#### 字符编码
- 当python代码中包含中文字符时，需要指定保存为UTF8编码,一般在文件开头加入下面的两行注释
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，在源代码中写的中文输出可能会有乱码
> Python3 的字符串使用Unicode，直接支持多语言
#### 数据类型和字符串
- 整型、浮点型、字符串、布尔值（`True\False`）、 空值（`None`）
- 关于字符串的函数
    - `ord(char)`: 函数获取字符的整数表示
    - `chr(num)`: 把编码转换为对应的字符
    - `len(str)` : 计算字符串的长度
- 字符串方法
    - `count(str)`: 返回str在string里出现的次数
    - `find(str)`: 检查str是否包含在字符串中，如果在返回索引，否则返回-1 
    - `replace(old, new [,max])`: 把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。
    - `split(sep)`: 以指定分隔符将字符串转为列表
    - `join`: 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
    - `lower()`: 转换字符串中所有大写字符为小写
    - `upper()`: 转换字符串中所有小写字符为大写
    - 占位符
        ```
        %d 整数
        %f 浮点数
        %s 字符串
        %x 十六进制整数
        ```

#### list和tuple
- list
    - `len(list)`: 获得list元素的个数
    - `list[index]`: 访问list中index位置的元素,index为-1直接获取最后一个元素
    - `list[start:end]`: 获得list中从索引为start到end不包含end之间的元素
    - `list.append(item)`: 往list中追加元素到末尾
    - `list.insert(index,item)`: 把元素插入到索引为index的位置
    - `list.pop([index])`: 删除list末尾的元素或删除指定位置的元素
- tuple
    > tuple和list非常类似，但是`tuple一旦初始化就不能修改`。它也没有append()，insert()这样的方法。
    因为tuple不可变，所以代码更安全。如果可能，`能用tuple代替list就尽量用tuple`。
    *`只有1个元素的tuple定义时必须加一个逗号`*,以免你误解成数学计算意义上的括号

#### 循环

    break 退出当前循环 
    continue 退出本轮循环，开始下一轮循环

#### dict 和 set

dict的`get`方法取值，如果不存在返回`None`

要删除一个key,使用`pop(key)`方法，对应的value也会被删除

`clear()`方法清空字典中所有元素，`del dict`删除一个字典

`set`和`dict`类似，但不存储value。由于key不能重复，所以set中没有重复的key

`add(key)`方法可以添加元素到set中

`remove(key)`方法可以删除元素

两个set可以做数学意义上的交集`(s1 & s2)`和并集`(s1 | s2)`

## 函数

- 函数定义: `def 函数名 ():`, 没有返回值默认返回`None`

- 空函数: 使用`pass`用来作为占位符，先放一个pass，让代码能运行起来。

- 返回多个值: 函数返回多值其实就是返回一个`tuple`

- 默认参数: *默认参数必须指向不变对象！*

- 可变参数: 
    - 定义: `def calc(*arguments):` 
    - 调用：`calc(2,3,4,5,6)`
    - 如果已经有了一个list或tuple，list或tuple前面加一个*号，可以把list或tuple的元素变成可变参数传进去 `calc(*nums)`

- 关键字参数: 关键字参数允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
    - 定义: `def person(name, age, **kw):`
    - 调用: 在调用时，可以只传入必选参数,也可以传入任意个数的关键字参数
    - 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去

```
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Neil', 23, **extra)
```

- 命名关键字参数：

如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。`def person(name, age, *, city, job):`

和关键字参数`**kw`不同，命名关键字参数需要一个特殊分隔符`*`，`*`后面的参数被视为命名关键字参数。

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了,但*命名关键字参数必须传入参数名*,如果没有传入参数名，调用将报错

- 参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：*必选参数、默认参数、可变参数、命名关键字参数和关键字参数*。

- 递归函数: 如果一个函数在内部调用自身本身，这个函数就是递归函数。

```
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
```

## 高级特性

- 迭代: 在Python中，迭代是通过`for ... in`来完成的

默认情况下，`dict`迭代的是`key`。如果要迭代`value`，可以用`for value in d.values()`，如果要同时迭代`key`和`value`，可以用`for k, v in d.items()`。

可以通过`collections`模块的`Iterable`类型判断一个对象是不是可迭代

Python内置的`enumerate`函数可以把一个`list`变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身

- 列表推导式

## 函数式编程

## 面向对象

## 错误和调试

## IO编程

## 异步IO

## 进程和线程

## 正则表达式

## 常用模块

### 内建模块

### 第三方模块

## 网络编程

## 访问数据库

## web开发
