#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 15:00
# @Author  : LiuPengjuan
# @Desc    : 列表生成器
# @File    : list.py
# @Software: PyCharm


def fib(max):
    n,a,b = 0,0,1
    while n < max:
        #print(b)
        yield b   #生成器
        a , b = b,a+b
        n = n+1
    return '$$$$$done$$$$$'

f = fib(10)
print(f.__next__())
print(f.__next__())
#print(fib(100))

#列表生成式
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value',e.value)
        break
