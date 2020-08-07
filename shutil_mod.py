#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 20:58
# @Author  : Liupj
# @Desc    : 
# @File    : shutil_mod.py
# @Software: PyCharm

import shutil
# f1 = open("readme.txt",encoding="utf-8")
# f2 = open("readme","w",encoding="utf-8")
# shutil.copyfileobj(f1,f2)

# shutil.copyfile("readme","file_dest")
# shutil.copystat("readme","file_dest")#copy权限
# shutil.copymode("readme","file_dest")#
# shutil.copy2("readme","file_dest")#
# shutil.copytree("a","a_2")# 递归复制
# shutil.rmtree("a_2")# 递归删除
# shutil.make_archive("shutil_archive_zip_test","zip","C:/Users/24434/Desktop/PythonText/day05")
import zipfile
z = zipfile.ZipFile("test.zip","w")
z.write("file_dest") #将其压缩到压缩包内
print("$$$$$")
z.write("readme") #将其压缩到压缩包内
z.close()