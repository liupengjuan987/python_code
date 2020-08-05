import sys
print(sys.getdefaultencoding())
str = "你好"
print(str.encode("gbk"))
str_gbk = str.encode("gbk")
print(str_gbk)
print(str_gbk.decode("gbk").encode("utf-8"))