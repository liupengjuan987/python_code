#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 10:18
# @Author  : LiuPengjuan
# @Desc    :  装饰器
# @File    : decorate.py
# @Software: PyCharm
import  time
def timmer(func):
    def warpper(*args,**kwargs):
        start_time= time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return warpper

@timmer
def func():
    time.sleep(3)
    print(" int the func..")
func()

#高阶函数
def bar():
    print("in the bar")

def foo(func):
    print(func)
    func()
foo(bar)

