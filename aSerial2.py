#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 15:37
# @Author  : Liupj
# @Desc    : 反序列化-load
# @File    : aSerial.py
# @Software: PyCharm
import json
# import pickle

def sayHi(name):
    print("Hello2,",name)
f = open("test.text","r")
#f = open("test.text","rb")


# data = pickle.load(f) #data = pickle.loads(f.read())
# print(data)
# print(data['func']('Songsa'))

# data = json.load(f)
data = json.loads(f.read())
print(data)
f.close()