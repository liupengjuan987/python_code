#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 11:06
# @Author  : Liupj
# @Desc    : 写configparse
# @File    : parseConf.py
# @Software: PyCharm

import configparser

config = configparser.ConfigParser() #configparser处理对象
config["default"]  = {
    'ServerAliveInterval':'45',
    'Compression':'yes',
    'CompressionLevel':'9'
}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11']='yes'

with open('example.ini','w') as configfile:
    config.write(configfile)
