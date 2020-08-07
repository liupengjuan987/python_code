#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 18:45
# @Author  : Liupj
# @Desc    : 目录结构
# @File    : direct.py
# @Software: PyCharm
import os
import sys
print(__file__)#打印当前路径 相对路径
print(os.path.abspath(__file__))#打印当前路径 相对路径
bse_dir = os.path.dirname(os.path.abspath(__file__))#打印当前路径的上级目录
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#打印当前路径的上级目录
sys.path.append(bse_dir)
from day05 import test
test.login()
# import day05
# test()