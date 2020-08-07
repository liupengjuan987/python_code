#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 22:07
# @Author  : Liupj
# @Desc    : shelve模块
# @File    : shelve_mod.py
# @Software: PyCharm
import shelve,datetime
d = shelve.open("shelve_test") #打开文件
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))
# info = {
#     "age":22,
#     "hobby":"play compute games"
# }
# name = ["SongSa","LiuPengjuan"]
#
# d["name"] = name
# d["info"] = info #持久化
# d['date'] = datetime.datetime.now()
d.close()