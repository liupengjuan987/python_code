#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 14:05
# @Author  : LiuPengjuan
# @Desc    : 装饰器
# @File    : decorate3.py
# @Software: PyCharm

import time

def timmer(func): #timmer(test1)
    def deco(*args,**kwargs):
        start_time = time.time()
        #return func
        func(*args,**kwargs)   #run test1()
        stop_time = time.time()
        print("the cost of func is %s" %(stop_time-start_time))
    return deco

@timmer  #test1 = timmer(test1)
def test1():
    time.sleep(2)
    print("in the test1")

@timmer  #test2 = timmer(test2)
def test2(name,age):
    #time.sleep(1)
    print("test2 :" ,name,age)
    print("in the test2")


test1()
test2('songsa',22)
# test1 = timmer(test1)
# test1()

#print(timmer(test1))  #打印出deco内存地址
# test1 = deco(test1)
# test1()
# deco(test2)

# test1()
# test2()