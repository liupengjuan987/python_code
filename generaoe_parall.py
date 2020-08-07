#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 17:00
# @Author  : LiuPengjuan
# @Desc    : 生产者 消费者  协程
# @File    : generaoe_parall.py
# @Software: PyCharm
import time
def consumer(name):
    print("%s 准备吃包子啦！" %name)
    while True:
        baozi = yield
        print("包子[%s]来了，被[%s]吃了" %(baozi,name))
c = consumer("Songsa")
c.__next__()
b1 = "韭菜馅"
c.send(b1)
#c.__next__()

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    for i in range(10):
        time.sleep(1)
        print("做了1个包子，分两半！")
        c.send(i)
        c2.send(i)
producer("Songss")
