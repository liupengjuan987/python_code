#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 18:27
# @Author  : Liupj
# @Desc    : random实现4位数字字母组合的验证码
# @File    : random_verycode.py
# @Software: PyCharm

import random

very_code = ''
for i in range(4):
    num = random.randint(0,4)
    if num == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
    # cur = random.randint(1,9) #[1,9]
    # very_code += str(cur)
    very_code += str(tmp)
print(very_code)