#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 15:37
# @Author  : Liupj
# @Desc    : 反序列化
# @File    : aSerial.py
# @Software: PyCharm
# import json
import pickle

def sayHi(name):
    print("Hello2,",name)
#f = open("test.txt","r")
f = open("test.text","rb")

#data = f.read()
# data = eval(f.read())

# data = json.loads(f.read())
# print(data['age'])
# f.close()
data = pickle.loads(f.read())
#print(data['age'])
print(data)
print(data['func']('Songsa'))
f.close()