#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 13:43
# @Author  : LiuPengjuan
# @Desc    : 高阶函数
# @File    : decorate2.py
# @Software: PyCharm
import time

def bar():
    time.sleep(1)
    print("in the bar...")
def test(func):
    start_time = time.time()
    #print(func) #bar  打印出内存地址
    func() #调用函数
    stop_time = time.time()
    print("cost of time is %s" %(stop_time-start_time))

def test2(func):
    print(func)
    return func
test2(bar())  # in the bar  ... None
#print(test2(bar))
#test(bar)
func = bar
#func()

#函数嵌套
def foo():
    print("in the foo")
    def bar():
        print(" in the bar")
    bar()

foo()
