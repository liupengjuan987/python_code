#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 9:43
# @Author  : Liupj
# @Desc    : 
# @File    : generators.py
# @Software: PyCharm

def fib(max):
    n , a , b = 0 , 0 ,1
    while n < max:
        #print(b)
        yield b
        a ,b = b ,a+b
        n = n+1
    return  '-done--'

#fib(10)
print(fib(10))
f = fib(10)
print(f.__next__())
print(f.__next__())

g = fib(10)
while True:
    try:
        x = next(g)
        print('G:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break


