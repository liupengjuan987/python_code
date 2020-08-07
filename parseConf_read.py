#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 11:15
# @Author  : Liupj
# @Desc    : 读configparse文件
# @File    : parseConf_read.py
# @Software: PyCharm

import configparser

conf = configparser.ConfigParser()
conf.read("example.ini")

print(conf.defaults()) #{'forwardx11': 'yes'}
print(conf.sections()) #['default', 'bitbucket.org', 'topsecret.server.com']
print(conf['default'])#<Section: default>
print(conf['bitbucket.org'])#<Section: bitbucket.org>
print(conf['bitbucket.org']['user'])# hg
print(conf['topsecret.server.com'])#<Section: topsecret.server.com>

#删除
sec = conf.remove_section('bitbucket.org')
conf.write(open('example.cfg','w'))