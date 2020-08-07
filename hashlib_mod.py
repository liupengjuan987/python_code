#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 11:27
# @Author  : Liupj
# @Desc    : haslib模块
# @File    : hashlib_mod.py
# @Software: PyCharm

# import hashlib
# m = hashlib.md5()
# m.update(b'hello')
# print(m.hexdigest()) #5d41402abc4b2a76b9719d911017c592
# m.update(b'it is me')
# print(m.hexdigest()) # 第一条拼接第二条加密后的：4e4e511166ca83f193aa89bb81082e62
# m.update(b'SongSa')
# print(m.hexdigest()) #0f00269df1e8b1fc9704139f3cc8455f
#
# m2 = hashlib.md5()
# m2.update(b'helloit is me')
# print(m2.hexdigest()) #4e4e511166ca83f193aa89bb81082e62
#
# s = hashlib.sha1()
# s.update(b'helloit is me')
# print(s.hexdigest()) #d728c718b8c58cc2da072753abc2103f6d2b8705

import hmac
h = hmac.new(b"1234","you are mrright".encode(encoding="utf-8"))
# h = hmac.new("1234","you are mrright")
print(h.digest())
print(h.hexdigest())

