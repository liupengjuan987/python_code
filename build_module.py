#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 18:59
# @Author  : Liupj
# @Desc    : 内置模块
# @File    : build_module.py
# @Software: PyCharm

import os
print(os.getcwd())

# os.chdir("C:\\Users\\24434\\Desktop\\PythonText") #不推荐
# print(os.getcwd())

os.chdir(r"C:\Users\24434\Desktop\PythonText") #推荐
print(os.getcwd())

print(os.curdir) # . 当前目录
print(os.pardir) # .. 上级目录

# print(os.makedirs(r"c:\a\b"))

#os.makedirs(r"c:\a\b") #递归创建目录结果
# os.mkdir(r"c:\a") #创建目录
# os.mkdir(r"c:\a\b") #创建目录

#os.removedirs(r"c:\a\b") #递归删除空目录文件夹
#os.rmdir(r"c:\a") #删除空目录文件夹
#os.rmdir(r"c:\a\b") #删除空目录文件夹
#os.removedirs(r"c:\a\b") #递归删除空目录文件夹

print(os.listdir(".")) #列出当前路径下所有文件 ['.git', '.idea', 'c', 'day04', 'day05']
print(os.listdir("..")) #列出上级路径下所有文件
print(os.listdir(r"d:")) # 列出指定路径下所有文件
print(os.stat(r"day04")) #
print(os.sep) # 分隔符 \
print("******")
print(os.linesep) # 换行分隔符  \r\n
print(os.pathsep) # 路径分隔符  ;
print(os.name) # nt：windows
print(os.path.split(r"C:\a\b\c.txt")) #('C:\\a\\b', 'c.txt')
print(os.path.dirname(r"C:\a\b\c.txt")) #C:\a\b
print(os.path.basename(r"C:\a\b\c.txt")) #c.txt
print(os.path.basename(r"C:\a\b\c")) #c
print(os.path.exists(r"C:\a\b\c")) #判断路径是否存在 False
print(os.path.isabs(r"C:\\d")) # 是否是绝对路径 True
print(os.path.isabs(r"d")) # 是否是绝对路径 false
print(os.path.isfile(r"d:")) # 是否是文件 false
print(os.path.getatime(r"C:\Users\24434\Desktop\PythonText\day05\moduler.py")) # 最后存取时间1596705475.221479
print(os.path.getmtime(r"C:\Users\24434\Desktop\PythonText\day05\moduler.py")) # 最后修改时间1596705471.430475
print(os.path.isfile(r"C:\Users\24434\Desktop\PythonText\day05\moduler.py")) # 是否是文件 True
print(os.path.join(r"C:\Users\24434","\Desktop\PythonText\day05\moduler.py")) # 将多个路径拼接返回
#print(os.path.abspath) # 绝对路径
#print(os.system("ipconfig")) # 用于执行命令
print(os.environ) #environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\24434\\AppData\\Roaming'})