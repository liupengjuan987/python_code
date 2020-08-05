# data = open("D:\homework\provinces.txt",encoding="utf-8").read()
# print(data)

# f = open("D:\homework\provinces.txt",encoding="utf-8") #文件句柄
# print(f.encoding)
# print(f.fileno())
# print(f.tell())  #当前位置
# print(f.readline())
# print(f.tell())
# print(f.seek(0))  #回到某一位置
# print(f.readline())

f = open("D:\homework\ptest.txt",'wb')#二进制文件
f.write("Hello lpj\n".encode())
f.close()
# f = open("D:\homework\ptest.txt",'rb')#二进制文件
# print(f.readline())
# print(f.readline())
# print(f.readline())

#f = open("D:\homework\ptest.txt",'r+',encoding="utf-8") #读写

# f = open("D:\homework\ptest.txt",'w+',encoding="utf-8") #写读 先创建文件 后写入
# f = open("D:\homework\ptest.txt",'a+',encoding="utf-8") #追加读读
# f.write("********************\n")
# f.write("********************\n")
# f.write("********************\n")
# print(f.tell())
# f.seek(10)
# print(f.tell())
# print(f.readline())
# f.write("should be at the beginning of the second line")
# print(f.readline())
# f.close()

# print(f.readline())
# print(f.readline())
# f.write("*********")  #追加写
# print(f.tell())
# print(f.readline())

# f.truncate(20) #从头截取多少个字符 此时seek()不好使
# f = open("D:\homework\ptest.txt",'a',encoding="utf-8") #文件句柄
# f.truncate(20) #从头截取多少个字符 此时seek()不好使

# data = f.read()
# data2 = f.read()
# print(data)
# print("************")
# print(data2)

# for line in f:  #一行一行读 内存中只保存这一行  效率最高  迭代器
#     #print(line.strip())
#     pass
# print(type(f))
