#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 17:29
# @Author  : Liupj
# @Desc    : 格式化时间
# @File    : time.py
# @Software: PyCharm

import time,datetime  #DST夏令时
print(datetime.date)
print(datetime.time)
print(datetime.datetime.now()+datetime.timedelta(hours=3))#获取几小时后的时间
print(datetime.datetime.now()+datetime.timedelta(hours=-3))#获取几小时前的时间
print(datetime.datetime.now()+datetime.timedelta(3))#获取几天后的时间
print(datetime.datetime.now()+datetime.timedelta(-3))#获取几天前的时间
print(datetime.datetime)
print(datetime.datetime.now())#获取当前时间
stamp = time.time()
print(stamp)
print(time.localtime())  #dst 时区
#print(help(time))
print(time.timezone/3600)
print(time.gmtime())
print(time.daylight)#是否使用夏令时 0 未使用
print(time.altzone)  #UTC  DST夏令时 差值
date = time.localtime()
print(date.tm_year)
print(date.tm_mon)
print(time.mktime(date))
print(time.ctime())  #second to string
print("******")
print(time.asctime(date))#struct_time-->String
print(time.asctime())#struct_time-->String
print(time.strftime("%Y-%m-%d %H:%M:%S",date)) #("格式",struct_time)-->格式化的字符串
print(time.strptime('2020-08-06 17:49:29',"%Y-%m-%d %H:%M:%S"))#("格式化的字符串"，“格式”)->struct_time