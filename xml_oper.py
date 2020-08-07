#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 22:20
# @Author  : Liupj
# @Desc    : xml处理
# @File    : xml_oper.py
# @Software: PyCharm

import xml.etree.cElementTree as ET
tree = ET.parse("txt.xml")
root = tree.getroot()
#print(root) #<Element 'xml' at 0x000002078005CA90>
#print(root.tag) #xml

#遍历xml文档
# for child in root:
#     print(child.tag,child.attrib)
#     for i in child:
#         #print(i)
#         print(i.tag,i.text,i.attrib)

#只遍历 节点
# for node in root.iter("small"):
#     print(node.tag,node.text)

#修改
# for node in root.iter('small'):
#     new_small= int(node.text) +1  #运算
#     node.text = str(new_small)
#     node.set("updated_by","LPj")#增加attr
#
# tree.write("txt.xml")#可写回原文件/新文件

#删除
for div in root.findall('div'):
    rank = int(div.find('rank').text)
    if rank > 50:
        root.remove(div)

tree.write('output.xml')