#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 10:19
# @Author  : Liupj
# @Desc    : 生产者 消费者
# @File    : Prod_Consu.py
# @Software: PyCharm

import time
def consumer(name):
    print("%s准备吃包子啦"%(name))
    while True:
        baozi = yield
        print("【%s】包子来了，被【%s】吃了" %(baozi,name))

c = consumer("Songsa")
c.__next__()  #仅调用yield

b1 = "韭菜馅"
c.send(b1)  #调用yield 并给其传值
#c.__next__()
def producer(name):
     c = consumer('A')
     c2 = consumer('B')
     c.__next__()
     c2.__next__()
     print("老子开始准备包子啦！")
     for i in range(10):
         time.sleep(1)
         print("做了2个包子！")
         c.send(i)
         c2.send(i)

producer('Songsa')
