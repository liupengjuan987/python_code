#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 20:01
# @Author  : LiuPengjuan
# @Desc    : 第三周作业：对配置文件进行查询 新增 删除操作  查有几个结点：打印结点个数 输入要查找的内容>打印出下边内容
# @File    : crud.py
# @Software: PyCharm

# print("********1.Update********")
print("********2.Delete********")
print("********3.Search********")
print("********4.Added********")
data= open('D:\\homework\\3-HAProxy.txt', 'a+', encoding='utf-8')
for line in data:
    print(line)
num = int(input("********请选择操作********"))
# if num == 1:
#     str=input("请输入要更新的内容：")
#     msg = eval(str)
#     f.write(msg)
#     print("文件已更新")
if num == 2:
    str = input("请输入要删除的内容：（roundobin）")
    if str in data:
        data.truncate()
    print("内容内容已成功删除")
if num == 3:
    str=input("请输入要查找的内容static/dynamic：")
    if str in data:
        print("要查找的内容如下：")
if num == 4:
    str=input("请输入增加内容：")
    f.write(str)
    print("内容已添加")

arg = {
     'backend':'www.baidu.com',
     'record':{
         'server':'192.18.1.2',
         'weight':20,
         'maxconn':30
     }
 }

