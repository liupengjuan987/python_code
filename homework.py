# f = open("info.txt","r", encoding='utf-8')
# lines=f.readline()
# # print(lines)
# list=lines.split(",")
# print(list)
# name=list[0]
# print(list[0])
# #password=list[1]
# #print(name,password)
# f.close()
with open('info.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# for index in range(len(lines)):
#     line = lines[index]
#     info = line.split(",")
#     name = info[0]
#     pwd=info[1]
#     if name=="songsa":
#         print(name, pwd)

# with open('info.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#
#     # name=lines[0]
#     # password=lines[1]
#     #print(name,password)
    count=0
    for i in range (3):
        username=input("username:")
        passwd=input("passwd:")
        # log = open("log.txt", "w") #保存登录日志
        # log.write(username)
        # log.write("\n")
        # log.close()
        eor = open("name.txt", "r", encoding="utf-8")#查看锁定用户
        info = eor.readlines()
        for index in range(len(info)):
            name = info[index].strip()
            #print(len(username),len(name))
            if username==name:   #被锁用户
                print("your account is locked,please ask admin for help!")
                break
        else:  #未被锁定
            for index in range(len(lines)):
                line = lines[index]
                info = line.split(",")
                name = info[0]
                password = info[1].strip()
                if username == name and password == passwd: #用户名 密码正确
                    print("Welcome user {username} login".format(username=name))
                    break
            else:
                print("invalid name or password")
    else:  #超过3次
        print("your account is locked!")
        error=open("name.txt","w")
        error.write(username)
        error.write("\n")
        error.close()



