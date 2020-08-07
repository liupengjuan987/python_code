#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 17:14
# @Author  : Liupj
# @Desc    : 导入优化
# @File    : Dul_import.py
# @Software: PyCharm
#优化原理：import是遇到一次调用，将代码解释一次
#from import 直接将代码拿来
from moduler import sayHi as hi

def welcome():
    hi()
    print("in the welcome")

def sayBye():
    hi()
    print("in the sayBye")
# import moduler
# def welcome():
#     moduler.sayHi()
#     print("in the welcome")
#
# def sayBye():
#     moduler.sayHi()
#     print("in the sayBye")