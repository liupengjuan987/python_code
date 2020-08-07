#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 16:09
# @Author  : Liupj
# @Desc    : 序列化-dump
# @File    : serial2.py
# @Software: PyCharm
# import pickle
import json
def sayHi(name):
    print("Hello,",name)
info = {
    'name': 'Songsa',
    'age': 23,
    # 'func': sayHi
}
# f = open("test.text","wb")
f = open("test.text","w")
# pickle.dump(info,f)
f.write(json.dumps(info))
info['age'] = 22
# pickle.dump(info,f)
f.write(json.dumps(info))
f.close()