#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 11:43
# @Author  : LiuPengjuan
# @Desc    : 装饰器 -加强版
# @File    : decorate_H.py
# @Software: PyCharm
name = "Songsa"
passwd = "521"
def auth(auth_type):
    print("auth func:",auth_type)
    def outwrapper(func):
        #def wrapper(*args,**kwargs):
        def wrapper():
            # print("wrapper func args:",*args,**kwargs)
            if auth_type == 'local':
                username = input("username:").strip()
                password = input("password:").strip()
                if username == name and password == passwd:
                    print("\033[32:1mUser has passed authntication\033[0m")
                    #res = func(*args, **kwargs)
                    res = func()
                    print("after authentication...")
                    return res
                else:
                    exit("\033[31:1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print("搞毛线？不会")
        return wrapper
    return outwrapper

# @auth
def index():
    print("Welcom to the index page")

@auth(auth_type="local")
def home():
    print("Welcom to the home page")
    return "from home "

@auth(auth_type="ldap")
def help():
    print("Welcom to the help page")

index()
home()
help()