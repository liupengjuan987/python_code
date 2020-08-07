#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 13:17
# @Author  : Liupj
# @Desc    : 正则表达式
# @File    : re_test.py
# @Software: PyCharm

import re
res = re.match("^Song","SongSa521") #match：从头开始匹配
res2 = re.search("[0-9]+","S23ongS56a521") #match：匹配到一个就返回
res3 = re.search("abc|ABC","ABCdabdc") #match：匹配到一个就返回
res4 = re.split("[0-9]+","3AB4Cd6a8bdc") #
res5 = re.sub("[0-9]+","|","3AB4Cd6a8bdc") #
print(res5)
res = re.findall("[0-9]{1,3}","S345ong67Sa521") #match：匹配所有 findall()没有Group方法
res2 = re.match("^Song\d+","Song233Sa521") #<re.Match object; span=(0, 4), match='Song'>
print(res2.group()) #匹配到的：Song
print(re.match("^aSong","SongSa521")) #None