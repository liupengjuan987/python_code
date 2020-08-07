#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 11:34
# @Author  : Liupj
# @Desc    : 内置函数
# @File    : build_in.py
# @Software: PyCharm
import functools
print(all([0,1,3,6,8]))  #False 全真 才真
print(any([1,3,0])) #有一个为真 就真
a = ascii([1,2,"你好！"])  #将内存对象变为可打印字符串
print(type(a),[a])
print(bin(1))  #十进制转二进制
print(bin(255))
print(bool(1))
print(bool(0))
a = bytes("abcdefg",encoding='utf-8')
b = bytearray("abcdefg",encoding='utf-8')
print(a)
print(b[0])
b[1] = 200
print(b)
print(a.capitalize(),a) #字符串不能修改
print(callable([])) #
def sayhi():pass
print(callable(sayhi))
print("######")
print(chr(99))    #c   ascii -->alp
print(ord('A'))  #65   alp -->ascii

code = "for i in range(10):print(i)"
# c = compile(code,'','exec')
# exec(c)
exec(code)

print("******")
program = "1+3*4/6"
p = compile(program,'','eval')
print(eval(p))
# eval(program)
print(divmod(5,3)) # / %

(lambda  n: print(n))(5)

#cal  = lambda  n: print(n**n)  #只能处理简单的
cal  = lambda  n: 3 if n < 5 else n   #只能处理简单的
cal(5)

#res = filter(lambda n:n>5 ,range(10))
#res = map(lambda n:n*n ,range(10))
#res = [lambda n:n*n for n in range(10)]

# for i in res:
#     print(i)

res = functools.reduce(lambda x, y: x + y, range(10))#累加
print(res)

a = frozenset([1,2,5,666,778,990,3,6,5])
print(globals())#当前程序中所有变量的k-v


def test():
    local_var = 333
    print(locals())
test()
# print(globals())
# print(globals().get('local_var'))

print(round(1.34982,3))#保留几位小数
print(round(1.34912,3))#保留几位小数
slice(2,4,None)
d = range(20)
d[slice(2,4)]
print(d)

a = {3:2,4:0,-8:6,99:23,5:1}
#b = sorted(a)  #只按key排序
b = sorted(a.items())#按key排序
b = sorted(a.items(),key=lambda  x:x[1])#按value排序

#print(a)
print(b)

a = [1,3,5,7,9]
b = ['a','b','c','d']
for i  in zip(a,b):
    print(i)
#print(zip(a,b))

import decorator
__import__('decorator')