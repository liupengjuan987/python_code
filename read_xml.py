#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 10:26
# @Author  : Liupj
# @Desc    : 创建xml
# @File    : read_xml.py
# @Software: PyCharm

import xml.etree.ElementTree as ET

new_xml = ET.Element("name_list")#根节点
personInfo = ET.SubElement(new_xml,"personInfo",attrib={"enrolled":"yes"})
name = ET.SubElement(personInfo,"name")
name.text  = "SongSa"
age = ET.SubElement(personInfo,"age",attrib={"checked":"no"})
sex = ET.SubElement(personInfo,"sex")
age.text = '33'

personInfo2 = ET.SubElement(new_xml,"personInfo",attrib={"enrolled":"no"})
name2 = ET.SubElement(personInfo2,"name")
name2.text  = "LiuPj"
age = ET.SubElement(personInfo2,"age")
age.text = '16'

et = ET.ElementTree(new_xml) #生成文档对象
et.write("test.xml",encoding="utf-8",xml_declaration=True)
ET.dump(new_xml)#打印生成的格式
