#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 20:06
# @Author  : Liupj
# @Desc    : 模块调用
# @File    : test.py
# @Software: PyCharm
import moduler,os,sys

import moduler,moduler_test
from moduler import sayHi as hi
#import与from import *区别：import调用方法时要加模块名 from import *相当于将代码拿过来了
#导入包 实际就是执行__Init__文件
print(moduler.name)
# moduler.syaHi()
#print(moduler.syaHi()) #None

def sayHi():
    print("Welcome to the test !")
sayHi()
hi()
#不同目录下导入 先将目录加入到path中
print(__file__)
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path)
sys.path.append(path)
import day04.atm_4 #正确打开方式
day04.atm_4.oper()

# import day04 #也不行
# day04.atm_4.oper()

#  import day04 #也不行
# day04.atm_4.oper()

# import atm_4  #虽然将路径加入path 但是仍要写包.模块
# atm_4.oper()

# def login():
#     print("Welcome")