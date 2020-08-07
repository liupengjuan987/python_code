role=input("请选择身份>商家/用户:")
logger={}
if role == "用户":
    name=input("请输入用户名：")
    with open("D:/homework/user.txt",'r') as f:
        info = f.readlines()
        #print(info)
        for i in range(len(info)):
            #print(info[i])
            if name != info[i]:
                salary=int(input("请输入工资："))
                with open("D:/homework/saler.txt") as f:
                    prod=f.readlines()
                    for index,item in enumerate(prod):
                        print(index,item)
                num=input("请选择要购买的商品编号/按q推出：")
                if num == 'q':
                    exit()
                elif int(num) <= salary :
                    num =int(num)
                    salary -= prod[num]
                    print("已购买商品:%s 您的余额为：%s"%(prod[index],salary))
                    with open("log.txt",'a',encoding='utf-8') as f:
                        logger.append(name)
                        logger.append(salary)
                        logger.append(prod[index])
                        f.write(logger)
elif role == "商家":
    with open("D:/homework/saler.txt") as f:
        f.read()
else:
    print("输入有误，请查正后再输")
