#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 10:34
# @Author  : Liupj
# @Desc    : 迭代器
# @File    : Iterator.py
# @Software: PyCharm
import collections.abc
print(isinstance([], collections.abc.Iterable)) #True
print(isinstance('abc', collections.abc.Iterable)) #True
print(isinstance({}, collections.abc.Iterable)) #True
a = [1,2,3]
print(dir(a))  #dir查看某元素所有可调用方法  有next方法 就是迭代器

print(isinstance((x for x in range(5)),collections.abc.Iterator)) #生成器就是迭代器 因为有next方法，反之不一定
print(isinstance([], collections.abc.Iterator)) #false
print(isinstance({}, collections.abc.Iterator)) #false
print(isinstance((), collections.abc.Iterator)) #false
b = iter(a)  #通过iter将可迭代对象转换成迭代器
print(b.__next__())
print(isinstance(b,collections.abc.Iterator)) #True