#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 15:35
# @Author  : Liupj
# @Desc    : 序列化
# @File    : Serial.py
# @Software: PyCharm
# import  json
import pickle
def sayHi(name):
    print("Hello,",name)
info = {
    'name':'Songsa',
    'age':23,
    'func':sayHi
}
f = open("test.text","wb")
print(pickle.dumps(info))
f.write(pickle.dumps(info))
# f = open("test.txt","w")
# # f.write(str(info))
# print(json.dumps(info))
# f.write(json.dumps(info))
# f.close()