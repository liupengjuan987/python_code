#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 18:14
# @Author  : Liupj
# @Desc    : 随机
# @File    : random_num.py
# @Software: PyCharm
import  random

print(random.random())
print(random.randint(1,3))
print(random.randRange(1,3))
print(random.choice('welcome'))
print(random.choice([2,5,6]))
print(random.sample('hello',2)) #随机取两位
print(random.uniform(1,3)) #指定区间随机取
all = [2,3,5,7,9,0]
all_af= random.shuffle(all)#洗牌
print(all_af)