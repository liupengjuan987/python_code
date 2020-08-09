#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 13:52
# @Author  : Liupj
# @Desc    : 压缩包内3个文件 从中提取出url 键值对形式写入json文件
# @File    : url_file.py
# @Software: PyCharm

import os,re,json
from unrar import rarfile #需要西安安装unrar

#解压文件
#得到文件路径
#读取并匹配到
#写成json

rf = rarfile.RarFile(r"C:\Users\24434\Desktop\data.rar", mode='r') # mode的值只能为'r'
rf_list = rf.namelist() # 得到压缩包里所有的文件
for f in rf_list:
    rf.extract(f, r"d:")  # 循环解压，将文件解压到指定路径
result=''
datas = {}
file = os.listdir(r"d:\data")
for i in file:
    index = os.path.splitext(i)
    if i.endswith("html"):
        key = int(index[0])
        print(key)
        with open(r"d:\data\%s"%(i),"r") as f:
            data = f.readline()
            for line in f:
                if line:
                    data = re.findall("'.*'", line)
                    if data:
                        for i in data:
                            if i.count("+") != 0:
                                pass
                            else:
                                result += i.strip().replace("'", "")
            print(result)
        datas[key]=result
        json_data = json.dumps(datas)
    else:
        print(json_data)

# with open(r"d:\data\1.html","r") as f:
#     data = f.readline()
#     for line in f:
#         if line:
#             data = re.findall("'.*'",line)
#             if data :
#                 for i in data:
#                     if i.count("+") != 0:
#                         pass
#                     else:
#                         result1 += i.strip().replace("'","")
#     print(result1)
# with open(r"d:\data\2.html","r") as f:
#     data = f.readline()
#     for line in f:
#         if line:
#             data = re.findall("'.*'", line)
#             if data:
#                 for i in data:
#                     if i.count("+") != 0:
#                         pass
#                     else:
#                         result2 += i.strip().replace("'", "")
#     print(result2)
# with open(r"d:\data\3.html","r") as f:
#     data = f.readline()
#     for line in f:
#         if line:
#             data = re.findall("'.*'", line)
#             if data:
#                 for i in data:
#                     if i.count("+") != 0:
#                         pass
#                     else:
#                         result3 += i.strip().replace("'", "")
#     print(result3)

# with open(r"d:\data\a.json","w+") as f:
#     data = {
#     "1":result1,
#     "2": result2,
#     "3": result3
#     }
#     f.write(json.dumps(data))


